# $Id$
#
# Package checking functions.  They come in two flavors:
# - individual package checks
# - set checks
#
# Individual checks need to be named "Check<something>", while set checks are named
# "SetCheck<something>".
#
# def CheckSomething(pkg_data, error_mgr, logger):
#   logger.debug("Checking something.")
#   error_mgr.ReportError("something-is-wrong")

import copy
import re
import os
import checkpkg
import opencsw
import pprint
import textwrap
import dependency_checks as depchecks
from Cheetah import Template

PATHS_ALLOWED_ONLY_IN = {
    # Leading slash must be removed.
    "CSWcommon": ["opt",
                  "opt/csw/man",
                  "opt/csw/doc",
                  "opt/csw/info",
                  "opt/csw/share/locale/locale.alias"],
    "CSWiconv": ["opt/csw/lib/charset.alias"],
    "CSWtexinfp": ["opt/csw/share/info/dir"],
}
MAX_DESCRIPTION_LENGTH = 100
LICENSE_TMPL = "/opt/csw/share/doc/%s/license"
OBSOLETE_DEPS = {
    # "CSWfoo": {
    #   "hint": "Do this...",
    #   "url": "http://www.opencsw.org/bugtrack/view.php?id=..."
    # },
    "CSWpython-rt": {
      "hint": "CSWpython-rt is deprecated, use CSWpython instead.",
      "url": "http://www.opencsw.org/bugtrack/view.php?id=4031"
    },
}
ARCH_RE = re.compile(r"(sparcv(8|9)|i386|amd64)")
MAX_CATALOGNAME_LENGTH = 20
MAX_PKGNAME_LENGTH = 20
ARCH_LIST = ["sparc", "i386", "all"]
VERSION_RE = r".*,REV=(20[01][0-9]\.[0-9][0-9]\.[0-9][0-9]).*"
DO_NOT_LINK_AGAINST_THESE_SONAMES = set(["libX11.so.4"])
DISCOURAGED_FILE_PATTERNS = (r"\.py[co]$",)
BAD_RPATH_LIST = [
    r'/opt/csw/lib/mysql/lib',
    r'/opt/csw/lib/mysql/lib/sparcv9',
    r'/opt/csw/lib/\$ISALIST',
    r'/opt/csw/lib/$$ISALIST',
    r'/opt/csw/lib/SALIST',
]
# Check ldd -r only for Perl modules
SYMBOLS_CHECK_ONLY_FOR = r"^CSWpm.*$"


def CatalognameLowercase(pkg_data, error_mgr, logger):
  catalogname = pkg_data["basic_stats"]["catalogname"]
  if catalogname != catalogname.lower():
    error_mgr.ReportError("catalogname-not-lowercase")
  if not re.match(r"^[\w_]+$", catalogname):
    error_mgr.ReportError("catalogname-is-not-a-simple-word")


def CheckDirectoryPermissions(pkg_data, error_mgr, logger):
  for entry in pkg_data["pkgmap"]:
    if (entry["type"] == "d"
          and
        entry["mode"] != "?"
          and
        entry["mode"][1] == "6"):
      error_mgr.ReportError("executable-bit-missing-on-a-directory",
                            entry["path"])


def CheckNonCswPathsDirectoryPerms(pkg_data, error_mgr, logger):
  for entry in pkg_data["pkgmap"]:
    if entry["user"] == "?" or entry["group"] == "?" or entry["mode"] == "?":
      if entry["path"].startswith("/opt/csw"):
        error_mgr.ReportError("pkgmap-question-mark-perms-in-opt-csw", entry["path"])


def CheckPerlLocal(pkg_data, error_mgr, logger):
  perllocal_re = re.compile(r'/perllocal.pod')
  for entry in pkg_data["pkgmap"]:
    if entry["path"]:
      if re.search(perllocal_re, entry["path"]):
        error_mgr.ReportError("perllocal-pod-in-pkgmap", entry["path"])


def CheckMultipleDepends(pkg_data, error_mgr, logger):
  new_depends = set()
  for pkgname, desc in pkg_data["depends"]:
    if pkgname in new_depends:
      error_mgr.ReportError("dependency-listed-more-than-once", pkgname)
    new_depends.add(pkgname)


def CheckDescription(pkg_data, error_mgr, logger):
  pkginfo = pkg_data["pkginfo"]
  desc = checkpkg.ExtractDescription(pkginfo)
  if not desc:
    error_mgr.ReportError("pkginfo-description-missing")
  else:
    if len(desc) > MAX_DESCRIPTION_LENGTH:
      error_mgr.ReportError("pkginfo-description-too-long", "length=%s" % len(desc))
    if not desc[0].isupper():
      error_mgr.ReportError("pkginfo-description-not-starting-with-uppercase",
                            desc)


def CheckCatalogname(pkg_data, error_mgr, logger):
  pkginfo = pkg_data["pkginfo"]
  catalogname = pkginfo["NAME"].split(" ")[0]
  catalogname_re = r"^([\w\+]+)$"
  if not re.match(catalogname_re, catalogname):
    error_mgr.ReportError("pkginfo-bad-catalogname", catalogname)


def CheckSmfIntegration(pkg_data, error_mgr, logger):
  init_re = re.compile(r"/init\.d/")
  for entry in pkg_data["pkgmap"]:
    if not entry["path"]:
      continue
    if not re.search(init_re, entry["path"]):
      continue
    if entry["class"] != "cswinitsmf":
      error_mgr.ReportError(
          "init-file-missing-cswinitsmf-class",
          "%s class=%s" % (entry["path"], entry["class"]))


def SetCheckLibraries(pkgs_data, error_mgr, logger):
  """Second versionof the library checking code.

  1. Collect all the data from the FS:
     {"<basename>": {"/path/1": ["CSWfoo1"], "/path/2": ["CSWfoo2"]}}
     1.1. find all needed sonames
     1.2. get all the data for needed sonames
  2. Construct an overlay by applying data from the package set
  3. For each binary
     3.1. Resolve all NEEDED sonames
  """
  needed_sonames = []
  for pkg_data in pkgs_data:
    for binary_info in pkg_data["binaries_dump_info"]:
      needed_sonames.extend(binary_info["needed sonames"])
  needed_sonames = sorted(set(needed_sonames))
  # Finding candidate libraries from the filesystem (/var/sadm/install/contents)
  path_and_pkg_by_soname = {}
  for needed_soname in needed_sonames:
    path_and_pkg_by_soname[needed_soname] = error_mgr.GetPathsAndPkgnamesByBasename(
        needed_soname)
  # Adding overlay based on the given package set
  # TODO: Emulate package removal
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    for binary_info in pkg_data["binaries_dump_info"]:
      soname = binary_info["soname"]
      binary_path, basename = os.path.split(binary_info["path"])
      if not binary_path.startswith('/'):
        binary_path = "/" + binary_path
      if soname not in path_and_pkg_by_soname:
        path_and_pkg_by_soname[soname] = {}
      path_and_pkg_by_soname[soname][binary_path] = [pkgname]
  # Resolving sonames for each binary
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    check_args = (pkg_data, error_mgr, logger, path_and_pkg_by_soname)
    req_pkgs_reasons = depchecks.Libraries(*check_args)
    req_pkgs_reasons.extend(depchecks.ByFilename(*check_args))
    missing_reasons_by_pkg = {}
    for pkg, reason in req_pkgs_reasons:
      if pkg not in missing_reasons_by_pkg:
        missing_reasons_by_pkg[pkg] = set()
      missing_reasons_by_pkg[pkg].add(reason)
    declared_deps = pkg_data["depends"]
    declared_deps_set = set([x[0] for x in declared_deps])
    req_pkgs_set = set([x[0] for x in req_pkgs_reasons])
    missing_deps = req_pkgs_set.difference(declared_deps_set)
    pkgs_to_remove = set()
    for regex_str in checkpkg.DO_NOT_REPORT_MISSING_RE:
      regex = re.compile(regex_str)
      for dep_pkgname in missing_deps:
        if re.match(regex, dep_pkgname):
          pkgs_to_remove.add(dep_pkgname)
    if pkgname in missing_deps:
      pkgs_to_remove.add(pkgname)
    logger.debug("Removing %s from the list of missing pkgs.", pkgs_to_remove)
    missing_deps = missing_deps.difference(pkgs_to_remove)
    surplus_deps = declared_deps_set.difference(req_pkgs_set)
    surplus_deps = surplus_deps.difference(checkpkg.DO_NOT_REPORT_SURPLUS)
    missing_deps_reasons = []
    for missing_dep in missing_deps:
      error_mgr.ReportError(pkgname, "missing-dependency", "%s" % (missing_dep))
      missing_deps_reasons.append((missing_dep, missing_reasons_by_pkg[missing_dep]))
    for surplus_dep in surplus_deps:
      error_mgr.ReportError(pkgname, "surplus-dependency", surplus_dep)
    namespace = {
        "pkgname": pkgname,
        "missing_deps": missing_deps_reasons,
        "surplus_deps": surplus_deps,
        "orphan_sonames": None,
    }
    t = Template.Template(checkpkg.REPORT_TMPL, searchList=[namespace])
    report = unicode(t)
    if report.strip():
      print report


def SetCheckDependencies(pkgs_data, error_mgr, logger):
  """Dependencies must be either installed in the system, or in the set."""
  known_pkgs = set(error_mgr.GetInstalledPackages())
  pkgs_under_check = [x["basic_stats"]["pkgname"] for x in pkgs_data]
  for pkgname in pkgs_under_check:
    known_pkgs.add(pkgname)
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    for depname, dep_desc in pkg_data["depends"]:
      if depname not in known_pkgs:
        error_mgr.ReportError(pkgname, "unidentified-dependency", depname)


def CheckDependsOnSelf(pkg_data, error_mgr, logger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  for depname, dep_desc in pkg_data["depends"]:
    if depname == pkgname:
      error_mgr.ReportError("depends-on-self")


def CheckArchitectureSanity(pkg_data, error_mgr, logger):
  basic_stats = pkg_data["basic_stats"]
  pkgname = basic_stats["pkgname"]
  pkginfo = pkg_data["pkginfo"]
  filename = basic_stats["pkg_basename"]
  arch = pkginfo["ARCH"]
  filename_re = r"-%s-" % arch
  if not re.search(filename_re, filename):
    error_mgr.ReportError("srv4-filename-architecture-mismatch",
                          "pkginfo=%s filename=%s" % (arch, filename))


def CheckActionClasses(pkg_data, error_mgr, logger):
  """Checks the consistency between classes in the prototype and pkginfo."""
  pkginfo = pkg_data["pkginfo"]
  pkgmap = pkg_data["pkgmap"]
  if "CLASSES" not in pkginfo:
    return
  pkginfo_classes = set(re.split(opencsw.WS_RE, pkginfo["CLASSES"]))
  pkgmap_classes = set()
  for entry in pkgmap:
    if entry["class"]:  # might be None
      pkgmap_classes.add(entry["class"])
  only_in_pkginfo = pkginfo_classes.difference(pkgmap_classes)
  only_in_pkgmap = pkgmap_classes.difference(pkginfo_classes)
  for action_class in only_in_pkginfo:
    error_mgr.ReportError("action-class-only-in-pkginfo", action_class)
  for action_class in only_in_pkgmap:
    error_mgr.ReportError("action-class-only-in-pkgmap", action_class)


def CheckLicenseFile(pkg_data, error_mgr, logger):
  """Checks for the presence of the license file."""
  # TODO: Write a unit test
  pkgmap = pkg_data["pkgmap"]
  catalogname = pkg_data["basic_stats"]["catalogname"]
  license_path = LICENSE_TMPL % catalogname
  pkgmap_paths = [x["path"] for x in pkgmap]
  if license_path not in pkgmap_paths:
    error_mgr.ReportError("license-missing")
    logger.info("See http://sourceforge.net/apps/trac/gar/wiki/CopyRight")


def CheckObsoleteDeps(pkg_data, error_mgr, logger):
  """Checks for obsolete dependencies."""
  deps = set(pkg_data["depends"])
  obsolete_pkg_deps = deps.intersection(set(OBSOLETE_DEPS))
  if obsolete_pkg_deps:
    for obsolete_pkg in obsolete_pkg_deps:
      error_mgr.ReportError("obsolete-dependency", obsolete_pkg)
      msg = ""
      if "hint" in OBSOLETE_DEPS[obsolete_pkg]:
        msg += "Hint: %s" % OBSOLETE_DEPS[obsolete_pkg]["hint"]
      if "url" in OBSOLETE_DEPS[obsolete_pkg]:
        if msg:
          msg += ", "
        msg += "URL: %s" % OBSOLETE_DEPS[obsolete_pkg]["url"]
      if not msg:
        msg = None
      logger.info(msg)


def CheckArchitectureVsContents(pkg_data, error_mgr, logger):
  """Verifies the relationship between package contents and architecture."""
  binaries = pkg_data["binaries"]
  pkginfo = pkg_data["pkginfo"]
  pkgmap = pkg_data["pkgmap"]
  arch = pkginfo["ARCH"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  reasons_to_be_arch_specific = []
  pkgmap_paths = [x["path"] for x in pkgmap]
  for pkgmap_path in pkgmap_paths:
    if re.search(ARCH_RE, str(pkgmap_path)):
      reasons_to_be_arch_specific.append((
          "archall-with-arch-paths",
          pkgmap_path,
          "path %s looks arch-specific" % pkgmap_path))
  for binary in binaries:
    reasons_to_be_arch_specific.append((
        "archall-with-binaries",
        binary,
        "package contains binary %s" % binary))
  if arch == "all":
    for tag, param, desc in reasons_to_be_arch_specific:
      error_mgr.ReportError(tag, param, desc)
  elif not reasons_to_be_arch_specific:
    logger.info("Package %s does not contain any binaries.", pkgname)
    logger.info("Consider making it ARCHALL = 1 instead of %s:", arch)
    logger.info("ARCHALL_%s = 1", pkgname)
    logger.info("However, be aware that there might be other reasons "
                "to keep it architecture-specific.")

def CheckFileNameSanity(pkg_data, error_mgr, logger):
  basic_stats = pkg_data["basic_stats"]
  revision_info = basic_stats["parsed_basename"]["revision_info"]
  catalogname = pkg_data["basic_stats"]["catalogname"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  if "REV" not in revision_info:
    error_mgr.ReportError("rev-tag-missing-in-filename")
  if len(catalogname) > MAX_CATALOGNAME_LENGTH:
    error_mgr.ReportError("catalogname-too-long")
  if len(pkgname) > MAX_PKGNAME_LENGTH:
    error_mgr.ReportError("pkgname-too-long")
  if basic_stats["parsed_basename"]["osrel"] == "unspecified":
    error_mgr.ReportError("osrel-tag-not-specified")


def CheckPkginfoSanity(pkg_data, error_mgr, logger):
  """pkginfo sanity checks.

if [ "$maintname" = "" ] ; then
  # the old format, in the DESC field
  maintname=`sed -n 's/^DESC=.*for CSW by //p' $TMPFILE`

  # Since the DESC field has been coopted, take
  # description from second half of NAME field now.
  desc=`sed -n 's/^NAME=[^ -]* - //p' $TMPFILE`
else
  if [ "$desc" = "" ] ; then
    desc=`sed -n 's/^NAME=[^ -]* - //p' $TMPFILE`
  fi
fi

software=`sed -n 's/^NAME=\([^ -]*\) -.*$/\1/p' $TMPFILE`
version=`sed -n 's/^VERSION=//p' $TMPFILE`
desc=`sed -n 's/^DESC=//p' $TMPFILE`
email=`sed -n 's/^EMAIL=//p' $TMPFILE`
maintname=`sed -n 's/^VENDOR=.*for CSW by //p' $TMPFILE`
hotline=`sed -n 's/^HOTLINE=//p' $TMPFILE`
basedir=`sed -n 's/^BASEDIR=//p' $TMPFILE`
pkgarch=`sed -n 's/^ARCH=//p' $TMPFILE|head -1`

if [ "$software" = "" ] ; then errmsg $f: software field not set properly in NAME ; fi
if [ "$pkgname" = "" ] ; then errmsg $f: pkgname field blank ; fi
if [ "$desc" = "" ] ; then errmsg $f: no description in either NAME or DESC field ; fi
if [ ${#desc} -gt 100 ] ; then errmsg $f: description greater than 100 chars ; fi
if [ "$version" = "" ] ; then errmsg $f: VERSION field blank ;  fi
if [ "$maintname" = "" ] ; then errmsg $f: maintainer name not detected. Fill out VENDOR field properly ; fi
if [ "$email" = "" ] ; then errmsg $f: EMAIL field blank ; fi
if [ "$hotline" = "" ] ; then errmsg $f: HOTLINE field blank ; fi
  """
  catalogname = pkg_data["basic_stats"]["catalogname"]
  pkgname = pkg_data["basic_stats"]["pkgname"]
  pkginfo = pkg_data["pkginfo"]
  # PKG, NAME, ARCH, VERSION and CATEGORY
  for parameter in ("PKG", "NAME", "ARCH", "VERSION", "CATEGORY"):
    if parameter not in pkginfo:
      error_mgr.ReportError("pkginfo-missing-parameter", parameter)
  if not catalogname:
    error_mgr.ReportError("pkginfo-empty-catalogname")
  if not pkgname:
    error_mgr.ReportError("pkginfo-empty-pkgname")
  if not "VERSION" in pkginfo or not pkginfo["VERSION"]:
    error_mgr.ReportError("pkginfo-version-field-missing")
  # maintname=`sed -n 's/^VENDOR=.*for CSW by //p' $TMPFILE`
  maintname = checkpkg.ExtractMaintainerName(pkginfo)
  if not maintname:
    error_mgr.ReportError("pkginfo-maintainer-name-not-set")
  # email
  if not pkginfo["EMAIL"]:
    error_mgr.ReportError("pkginfo-blank-email")
  # hotline
  if not pkginfo["HOTLINE"]:
    error_mgr.ReportError("pkginfo-hotline-blank")
  pkginfo_version = pkg_data["basic_stats"]["parsed_basename"]["full_version_string"]
  if pkginfo_version != pkginfo["VERSION"]:
    error_mgr.ReportError("filename-version-does-not-match-pkginfo-version")
  if re.search(r"-", pkginfo["VERSION"]):
    error_mgr.ReportError("pkginfo-minus-in-version")
  if not re.match(VERSION_RE, pkginfo["VERSION"]):
    msg = pkginfo["VERSION"]
    error_mgr.ReportError("pkginfo-version-wrong-format", msg)
  if pkginfo["ARCH"] not in ARCH_LIST:
    error_mgr.ReportError("pkginfo-nonstandard-architecture", pkginfo["ARCH"])


def CheckPstamp(pkg_data, error_mgr, logger):
  pkginfo = pkg_data["pkginfo"]
  if "PSTAMP" in pkginfo:
    if not re.match(checkpkg.PSTAMP_RE, pkginfo["PSTAMP"]):
      msg=("It should be 'username@hostname-timestamp', "
           "but it's %s." % repr(pkginfo["PSTAMP"]))
      error_mgr.ReportError("pkginfo-pstamp-in-wrong-format", pkginfo["PSTAMP"], msg)
  else:
    error_mgr.ReportError("pkginfo-pstamp-missing")


def DisabledCheckMissingSymbols(pkgs_data, error_mgr, logger):
  """Analyzes missing symbols reported by ldd -r.

  1. Collect triplets: pkgname, binary, missing symbol
  2. If there are any missing symbols, collect all the symbols that are provided
     by the set of packages.
  3. From the list of missing symbols, remove all symbols that are provided
     by the set of packages.
  4. Report any remaining symbols as errors.

  What indexes do we need?

  symbol -> (pkgname, binary)
  set(allsymbols)
  """
  missing_symbols = []
  all_symbols = set()
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    binaries = pkg_data["binaries"]
    for binary in binaries:
      for ldd_elem in pkg_data["ldd_dash_r"][binary]:
        if ldd_elem["state"] == "symbol-not-found":
          missing_symbols.append((pkgname,
                                  binary,
                                  ldd_elem["symbol"]))
      for symbol in pkg_data["defined_symbols"][binary]:
        all_symbols.add(symbol)
  # Remove symbols defined elsewhere.
  while missing_symbols:
    ms_pkgname, ms_binary, ms_symbol = missing_symbols.pop()
    if ms_symbol not in all_symbols:
      error_mgr.ReportError("symbol-not-found", "%s %s" % (ms_binary, ms_symbol))


def CheckBuildingUser(pkg_data, error_mgr, logger):
  pkgname = pkg_data["basic_stats"]["pkgname"]
  username = checkpkg.ExtractBuildUsername(pkg_data["pkginfo"])
  for entry in pkg_data["pkgmap"]:
    if entry["user"] and entry["user"] == username:
      error_mgr.ReportError("file-owned-by-building-user"
                            "%s, %s" % (entry["path"], entry["user"]))


def CheckDisallowedPaths(pkg_data, error_mgr, logger):
  """Checks for disallowed paths, such as common paths."""
  arch = pkg_data["pkginfo"]["ARCH"]
  # Common paths read from the file are absolute, e.g. /opt/csw/lib
  # while paths in pkginfo are relative, e.g. opt/csw/lib.
  common_paths = []
  for common_path in error_mgr.GetCommonPaths(arch):
    if common_path.startswith("/"):
      common_path = common_path[1:]
    common_paths.append(common_path)
  paths_only_allowed_in = copy.copy(PATHS_ALLOWED_ONLY_IN)
  paths_only_allowed_in["CSWcommon"] += common_paths
  paths_in_pkg = set()
  for entry in pkg_data["pkgmap"]:
    entry_path = entry["path"]
    if not entry_path:
      continue
    if entry_path.startswith("/"):
      entry_path = entry_path[1:]
    paths_in_pkg.add(entry_path)
  for pkgname in paths_only_allowed_in:
    if pkgname != pkg_data["basic_stats"]["pkgname"]:
      disallowed_paths = set(paths_only_allowed_in[pkgname])
      intersection = disallowed_paths.intersection(paths_in_pkg)
      logger.debug("Bad paths found: %s", intersection)
      for bad_path in intersection:
        error_mgr.ReportError("disallowed-path", bad_path)


def CheckLinkingAgainstSunX11(pkg_data, error_mgr, logger):
  for binary_info in pkg_data["binaries_dump_info"]:
    for soname in binary_info["needed sonames"]:
      if (".so" in binary_info["soname"]
          and
          soname in DO_NOT_LINK_AGAINST_THESE_SONAMES):
        error_mgr.ReportError("linked-against-discouraged-library",
                              "%s %s" % (binary_info["base_name"], soname))


def CheckDiscouragedFileNamePatterns(pkg_data, error_mgr, logger):
  patterns = [re.compile(x) for x in DISCOURAGED_FILE_PATTERNS]
  for entry in pkg_data["pkgmap"]:
    if entry["path"]:
      for pattern in patterns:
        if re.search(pattern, entry["path"]):
          error_mgr.ReportError("discouraged-path-in-pkgmap",
                                entry["path"])


def CheckBadPaths(pkg_data, error_mgr, logger):
  for regex in pkg_data["bad_paths"]:
    for file_name in pkg_data["bad_paths"][regex]:
      error_mgr.ReportError("file-with-bad-content", "%s %s" % (regex, file_name))


def CheckPkgchk(pkg_data, error_mgr, logger):
  if pkg_data["pkgchk"]["return_code"] != 0:
    error_mgr.ReportError("pkgchk-failed-with-code", pkg_data["pkgchk"]["return_code"])
    for line in pkg_data["pkgchk"]["stderr_lines"]:
      logger.warn(line)

def CheckRpath(pkg_data, error_mgr, logger):
  # for bad_rpath in BAD_RPATH_LIST:
  bad_rpath_set = set(BAD_RPATH_LIST)
  for binary_info in pkg_data["binaries_dump_info"]:
    for actual_rpath in binary_info["runpath"]:
      if actual_rpath in bad_rpath_set:
        error_mgr.ReportError("bad-rpath-entry",
                              "%s %s" % (binary_info["path"], actual_rpath))


def DisabledCheckForMissingSymbols(pkgs_data, debug):
  """Analyzes missing symbols reported by ldd -r.

  1. Collect triplets: pkgname, binary, missing symbol
  2. If there are any missing symbols, collect all the symbols that are provided
     by the set of packages.
  3. From the list of missing symbols, remove all symbols that are provided
     by the set of packages.
  4. Report any remaining symbols as errors.

  What indexes do we need?

  symbol -> (pkgname, binary)
  set(allsymbols)
  """
  errors = []
  missing_symbols = []
  all_symbols = set()
  for pkg_data in pkgs_data:
    pkgname = pkg_data["basic_stats"]["pkgname"]
    binaries = pkg_data["binaries"]
    for binary in binaries:
      for ldd_elem in pkg_data["ldd_dash_r"][binary]:
        if ldd_elem["state"] == "symbol-not-found":
          missing_symbols.append((pkgname,
                                  binary,
                                  ldd_elem["symbol"]))
      for symbol in pkg_data["defined_symbols"][binary]:
        all_symbols.add(symbol)
  # Remove symbols defined elsewhere.
  while missing_symbols:
    ms_pkgname, ms_binary, ms_symbol = missing_symbols.pop()
    if ms_symbol not in all_symbols:
      errors.append(checkpkg.CheckpkgTag(
        ms_pkgname, "symbol-not-found", "%s %s" % (ms_binary, ms_symbol)))
  return errors


def CheckForMissingSymbolsDumb(pkg_data, error_mgr, logger):
  """Analyzes missing symbols reported by ldd -r.

  Only makes sense for perl modules.
  """
  pkgname = pkg_data["basic_stats"]["pkgname"]
  if not re.match(SYMBOLS_CHECK_ONLY_FOR, pkgname):
    return
  found = False
  for binary_info in pkg_data["binaries_dump_info"]:
    for ldd_elem in pkg_data["ldd_dash_r"][binary_info["path"]]:
      if ldd_elem["state"] == "symbol-not-found":
        error_mgr.ReportError("symbol-not-found",
                              "e.g. %s misses %s" % (binary_info["path"], ldd_elem["symbol"]))
        found = True
        break
    if found:
      break
