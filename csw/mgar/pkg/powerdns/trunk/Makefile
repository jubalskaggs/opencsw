# PowerDNS
# $Id$
#
NAME = pdns
VERSION = 3.3
CATEGORIES = server
GARTYPE = v2

DESCRIPTION = An advanced DNS server with multiple backends
define BLURB
  PowerDNS is an advanced DNS server, which allows for several different
  backends. Current backends include MySQL, PostgreSQL, bind, etc.
endef

# Open issues:
# -llber
# timegm() in utils.hh ldapbackend
# endian.h net.c
# 
#   AR    libpolarssl.a
#   ar: creating libpolarssl.a
#     RL    libpolarssl.a
#     ar: one of [drqtpmx] must be specified
#     gmake[5]: *** [libpolarssl.a] Error 1 
#   ^^^ treba pouzit ranlib
#
# @@SYSCONFDIR@@
# asprintf http://blogs.everycity.co.uk/alasdair/2011/07/vasprintf-and-asprintf-on-solaris-10/
#
MASTER_SITES = http://downloads.powerdns.com/releases/
SPKG_SOURCEURL = http://www.powerdns.com/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += LICENSE
DISTFILES += cswpdns
PATCHFILES += 0003-Use-gar-instead-of-PATCHFILES += 0004-Use-PF_UNIX-instead-of-AF_LOCAL.patch
PATCHFILES += 0005-Correctly-determine-build-user-host.patch
PATCHFILES += 0006-Correct-definesead-of-ar-for-ranlib.patch

WORKSRC = $(WORKDIR)/$(NAME)-$(VERSION)

LICENSE = $(FILEDIR)/LICENSE
PACKAGING_PLATFORMS = solaris10-i386 solaris10-sparc

GARCOMPILER = GNU
NORUNPATH = 1

REINPLACEMENTS += usrlocaletc
REINPLACE_MATCH_usrlocaletc = /usr/local/etc
REINPLACE_WITH_usrlocaletc = /etc$(prefix)/pdns
REINPLACE_FILES_usrlocaletc = pdns/pdns.conf-dist

REINPLACEMENTS += usrlocallib
REINPLACE_MATCH_usrlocallib = /usr/local/lib
REINPLACE_WITH_usrlocallib = $(prefix)/lib/pdns
REINPLACE_FILES_usrlocallib = pdns/pdns.conf-dist

CONFIGURE_ARGS = $(DIRPATHS)
CONFIGURE_ARGS += --sysconfdir=/etc$(prefix)/pdns
CONFIGURE_ARGS += --libdir=$(prefix)/lib/pdns
CONFIGURE_ARGS += --with-lua=no
CONFIGURE_ARGS += --with-boost=/opt/csw/gxx
CONFIGURE_ARGS += --with-mysql=$(prefix)
CONFIGURE_ARGS += --with-mysql-lib=$(prefix)/lib
CONFIGURE_ARGS += --with-mysql-includes=$(prefix)/include
CONFIGURE_ARGS += --with-sqlite3
CONFIGURE_ARGS += --with-modules="ldap pipe remote geo gmysql gsqlite3"

EXTRA_CONFIGURE_ENV += "PKG_CONFIG=/opt/csw/bin/pkg-config"
EXTRA_CONFIGURE_ENV += "PKG_CONFIG_PATH=/opt/csw/lib/pkgconfig"

# Prepend Boost 1.49 installation in paths so we pick up the correct one
EXTRA_INC = /opt/csw/gxx/include
LDFLAGS +=LDFLAGS += -Wl,-B,direct
LDFLAGS += -Wl,-z,ignore= -L/opt/csw/gxx/lib

# PowerDNS does not have any "test" target
SKIPTEST = 1

PACKAGES = CSWpdns
CATALOGNAME_CSWpdns = powerdns
SPKG_DESCRUNTIME_DEP_PKGS_CSWpdns_sparc += CSWlibz1
_CSWpdns += CSWlibz1
RUNTIME_DEP_PKGS_CSWpdns += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWpdns +8 CSWlibmysqlclient15
RUNTIME_DEP_PKGS_CSWpdns += CSWlibstdc++6
RUNTIME_DEP_PKGS_CSWpdns += CSWlibboost-prog-opts1-49-0-gxx
RUNTIME_DEP_PKGS_CSWpdns += CSWlibboost-s13n1-49-0-gxx
RUNTIME_DEP_PKGS_CSWpdns += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWpdns += CSWlibldap-r2-4-2
RUNTIME_DEP_PKGS_CSWpdnsRUNTIME_DEP_PKGS_CSWpdns += $(RUNTIME_DEP_PKGS_CSWpdns_$(GARCH))
s += CSWlibsqlite3-0
BUILD_DEP_PKGS_CSWpdns += CSWmysql-dev
BUILD_DEP_PGKS_CSWpdns += CSWboostdevel
BUILD_DEP_PKGS_CSWpdns += CSWlibsqlite3-dev
BUILD_DEP_PGKS_CSWpdns += CSWopenldap-dev
BUILD_DEP_PGKS_CSWBUILD_DEP_PGKS_CSWpdns += CSWlibcurlS_CSWpdns += CSWlibz-dev

# These are not errors!
CHECKPKG_OVERRIDES_CSWpdns += catalogname-does-not-match-pkgname|pkgname=CSWpdns|catalogname=powerdns|expectCHECKPKG_OVERRIDES_CSWpdns += soname-unusedted-catalogname=pdns

INITSMF = /etc/opt/csw/init.d/cswpdns
PRESERVECONF = /etc/opt/csw/pdns/pdns.conf

post-install-modulated:
	@echo " ==> Installing Init Script"
	@ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	@ginstall -m 755 $(FILEDIR)/cswpdns $(DESTDIR)/etc/opt/csw/init.d/cswpdns
	@echo " ==> Moving config file"
	@mv $(DESTDIR)/etc$(prefix)/pdns/pdns.conf-dist $(DESTDIR)/etc$(prefix)/pdns/pdns.conf
	@$(MAKECOOKIE)

incl