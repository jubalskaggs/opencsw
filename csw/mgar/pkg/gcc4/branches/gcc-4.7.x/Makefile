# $Id$

NAME      = gcc
VERSION   = 4.7.2
GARTYPE = v2
BASE_VERSION = $(shell echo $(VERSION) | gsed -e 's/^\([0-9]\+\.[0-9]\+\)\(.*\)/\1/')
PKG_VERSION_TOKEN = gcc4
PKG_BASENAME = CSW$(PKG_VERSION_TOKEN)
# PKG_BASENAME = CSWgcc-$(subst .,-,$(BASE_VERION))

DESCRIPTION  = The GNU Compiler Collection
define BLURB
	The GNU Compiler Collection includes front ends for C, C++,
	Objective-C, Fortran, Java, and Ada, as well as libraries
	for these languages (libstdc++, libgcj,...).
endef

DISTFILES    = $(DISTNAME).tar.bz2
MASTER_SITES = $(GNU_MIRROR)/$(NAME)-$(VERSION)/
MASTER_SITES += http://ftp.heanet.ie/mirrors/gnu/gcc/$(NAME)-$(VERSION)/

LIBOBJC = 4

# We're not building GCC-4.7 on Solaris 9, because GCC-4.7 requires the
# sparcv8+ architecture.
# PACKAGING_PLATFORMS = solaris9-sparc solaris9-i386
PACKAGING_PLATFORMS += solaris10-sparc solaris10-i386

# there is  a problem with direct linking on amd64 libs
LINKER_DIRECT =

# GIT init takes a long time.
NOGITPATCH ?= 1

## Source URLs
VENDOR_URL = http://gcc.gnu.org

## Copyright File
LICENSE = COPYING3

BUILD_DEP_PKGS += CSWbinutils
BUILD_DEP_PKGS += CSWcloog-dev
BUILD_DEP_PKGS += CSWgnulinks
BUILD_DEP_PKGS += CSWlibgmp-dev
BUILD_DEP_PKGS += CSWlibmpc-dev
BUILD_DEP_PKGS += CSWlibmpfr-dev
BUILD_DEP_PKGS += CSWlibppl-dev
BUILD_DEP_PKGS += CSWlibz-dev

# Could be used to break out of the /opt/csw/$(PKG_VERSION_TOKEN) prefix
PROGRAM_SUFFIX = -$(BASE_VERSION)

## build options
# http://gcc.gnu.org/install/configure.html

CONFIGURE_ARGS += $(DIRPATHS)
CONFIGURE_ARGS += --enable-cloog-backend=isl
CONFIGURE_ARGS += --enable-java-awt=xlib
CONFIGURE_ARGS += --enable-languages=ada,c,c++,fortran,go,java,objc
CONFIGURE_ARGS += --enable-libada
CONFIGURE_ARGS += --enable-libssp
CONFIGURE_ARGS += --enable-nls
CONFIGURE_ARGS += --enable-objc-gc
CONFIGURE_ARGS += --enable-threads=posix
CONFIGURE_ARGS += --program-suffix=$(PROGRAM_SUFFIX)
CONFIGURE_ARGS += --with-cloog=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-gmp=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-included-gettext
CONFIGURE_ARGS += --with-ld=/usr/ccs/bin/ld
CONFIGURE_ARGS += --without-gnu-ld
CONFIGURE_ARGS += --with-libiconv-prefix=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-mpfr=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-ppl=$(BUILD_PREFIX)
CONFIGURE_ARGS += --with-system-zlib=$(BUILD_PREFIX)

# Using ccs/bin/bas on x86 results in this problem:
# http://gcc.gnu.org/bugzilla/show_bug.cgi?id=35531
CONFIGURE_ARGS_sparc += --with-as=/usr/ccs/bin/as
CONFIGURE_ARGS_sparc += --without-gnu-as
CONFIGURE_ARGS_i386 += --with-gnu-as
CONFIGURE_ARGS_i386 += --with-as=/opt/csw/bin/gas
CONFIGURE_ARGS += $(CONFIGURE_ARGS_$(GARCH))

# GCC can't be built in the same directory with the sources.
# It also can't be built in a subdirectory of the sources.
OBJDIR          = $(abspath $(WORKDIR)/objdir)

# bash must be used, otherwise:
# http://fixunix.com/solaris/490396-gcc-build-fails-cannot-compute-suffix-object-files.html
CONFIG_SHELL = /opt/csw/bin/bash
EXTRA_EXPORTS += CONFIG_SHELL

# Bootstrapping with Sun Studio has issues
# http://gcc.gnu.org/ml/gcc-help/2011-08/msg00191.html
GARCOMPILER = GNU

# There's a lot of failing checks. Probably a lot of porting work.
SKIPTEST ?= 1

# Used multiple times in package definitions
JAVA_LIB_VERSION = 13

ALTERNATIVES_PRIO = 470

PACKAGES = $(PKG_BASENAME)core
SPKG_DESC_$(PKG_BASENAME)core = GNU C compiler
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibcloog-isl2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibffi4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibgcc-s1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibgcj$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibgcj-tools$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibgij$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibgo0
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibgomp1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibitm1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibppl-c4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibssp0
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibz1

# checkpkg-undetectable dependencies
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWbinutils
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWcoreutils
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWggrep
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWgsed

ALTERNATIVES_$(PKG_BASENAME)core += $(PKG_VERSION_TOKEN)core
ALTERNATIVE_$(PKG_VERSION_TOKEN)core += $(bindir)/cpp gcc_core $(bindir)/cpp$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)
ALTERNATIVE_$(PKG_VERSION_TOKEN)core += $(bindir)/gcc gcc_core $(bindir)/gcc$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)core += $(bindir)/gcov gcc_core $(bindir)/gcov$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)core += $(bindir)/gccgo gcc_core $(bindir)/gccgo$(PROGRAM_SUFFIX)

# Because I can.
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-with-bad-content
CHECKPKG_OVERRIDES_$(PKG_BASENAME)g++ += file-with-bad-content
CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += file-with-bad-content
CHECKPKG_OVERRIDES_CSWlibgcj$(JAVA_LIB_VERSION) += file-with-bad-content
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += discouraged-path-in-pkgmap|$(libexecdir)/gcc/i386-pc-solaris2.9/$(VERSION)/liblto_plugin.la
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += discouraged-path-in-pkgmap|$(libexecdir)/gcc/sparc-sun-solaris2.9/$(VERSION)/liblto_plugin.la
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += discouraged-path-in-pkgmap|$(libexecdir)/gcc/sparc-sun-solaris2.10/$(VERSION)/liblto_plugin.la
CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += file-with-bad-content
CHECKPKG_OVERRIDES_$(PKG_BASENAME)gfortran += file-with-bad-content
# Due to complex regular expressions
CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += file-collision|$(includedir)/c++/$(VERSION)/sun/awt/CausedFocusEvent.h|$(PKG_BASENAME)g++|$(PKG_BASENAME)java
CHECKPKG_OVERRIDES_$(PKG_BASENAME)g++ += file-collision|$(includedir)/c++/$(VERSION)/sun/awt/CausedFocusEvent.h|$(PKG_BASENAME)g++|$(PKG_BASENAME)java
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += missing-dependency|CSWpython
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += surplus-dependency|CSWbinutils
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += surplus-dependency|CSWcoreutils
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += surplus-dependency|CSWggrep
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += surplus-dependency|CSWgsed

# Only man pages, so not a big problem. Alternatives could be used, but it
# requires rebuilding libffi.
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(mandir)/man3/ffi_call.3|$(PKG_BASENAME)core|CSWlibffi-dev
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(mandir)/man3/ffi.3|$(PKG_BASENAME)core|CSWlibffi-dev
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(mandir)/man3/ffi_prep_cif.3|$(PKG_BASENAME)core|CSWlibffi-dev

# The .a files are necessary
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += discouraged-path-in-pkgmap
CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += discouraged-path-in-pkgmap
CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += discouraged-path-in-pkgmap

CHECKPKG_OVERRIDES_$(PKG_BASENAME)gfortran += discouraged-path-in-pkgmap

# From the 'hopeless errors' department:
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/libffi.so|CSWgcc3javart|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/libgcc_s.so|CSWgcc3core|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/libgcj.so|CSWgcc3javart|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/libobjc.so|CSWgcc3objcrt|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/sparcv9/lib-gnu-awt-xlib.so|CSWgcc3javart|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/sparcv9/libffi.so|CSWgcc3javart|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/sparcv9/libgcj.so|CSWgcc3javart|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/sparcv9/libobjc.so|CSWgcc3objcrt|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += file-collision|$(libdir)/libobjc.so|CSWgcc3objcrt|$(PKG_BASENAME)objc
CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += file-collision|$(libdir)/sparcv9/libobjc.so|CSWgcc3objcrt|$(PKG_BASENAME)objc
CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += file-collision|$(libdir)/lib-gnu-awt-xlib.so|CSWgcc3javart|$(PKG_BASENAME)core

# Some static libraries are required to build binaries with gcc, for example
# libgcc.a and libgcc_eh.a. Otherwise: ld: fatal: library -lgcc: not found
MERGE_EXCLUDE_LIBTOOL =
MERGE_EXCLUDE_STATICLIBS =
EXTRA_MERGE_EXCLUDE_FILES = $(libdir)/libiberty\.a

# Catch-all package

PACKAGES += CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION)
CATALOGNAME_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) = lib_gnu_awt_xlib$(JAVA_LIB_VERSION)
PKGFILES_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),lib-gnu-awt-xlib\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += $(DESCRIPTION), lib-gnu-awt-xlib.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME) += CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += CSWlibstdc++$(LIBSTDCXX_VERSION)
RUNTIME_DEP_PKGS_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += CSWlibgcc-s1

PACKAGES += CSWlibffi4
CATALOGNAME_CSWlibffi4 = libffi4
PKGFILES_CSWlibffi4 += $(call baseisadirs,$(libdir),libffi\.so\.4(\.\d+)*)
SPKG_DESC_CSWlibffi4 += $(DESCRIPTION), libffi.so.4
RUNTIME_DEP_PKGS_$(PKG_BASENAME) += CSWlibffi4
RUNTIME_DEP_PKGS_CSWlibffi4 += CSWlibgcc-s1

PACKAGES += CSWlibgcc-s1
CATALOGNAME_CSWlibgcc-s1 = libgcc_s1
PKGFILES_CSWlibgcc-s1 += $(call baseisadirs,$(libdir),libgcc_s\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibgcc-s1 += $(DESCRIPTION), libgcc_s.so.1
RUNTIME_DEP_PKGS_$(PKG_BASENAME) += CSWlibgcc-s1

PACKAGES += CSWlibgcj-tools$(JAVA_LIB_VERSION)
CATALOGNAME_CSWlibgcj-tools$(JAVA_LIB_VERSION) = libgcj_tools$(JAVA_LIB_VERSION)
PKGFILES_CSWlibgcj-tools$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),libgcj-tools\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_CSWlibgcj-tools$(JAVA_LIB_VERSION) += $(DESCRIPTION), libgcj-tools.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME) += CSWlibgcj-tools$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWlibgcj-tools$(JAVA_LIB_VERSION) += CSWlibgcc-s1
RUNTIME_DEP_PKGS_CSWlibgcj-tools$(JAVA_LIB_VERSION) += CSWlibgcj$(JAVA_LIB_VERSION)

PACKAGES += CSWlibgcj$(JAVA_LIB_VERSION)
CATALOGNAME_CSWlibgcj$(JAVA_LIB_VERSION) = libgcj$(JAVA_LIB_VERSION)
PKGFILES_CSWlibgcj$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),libgcj\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_CSWlibgcj$(JAVA_LIB_VERSION) += $(DESCRIPTION), libgcj.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWlibgcj$(JAVA_LIB_VERSION) += CSWlibgcc-s1

PACKAGES += CSWlibgfortran3
CATALOGNAME_CSWlibgfortran3 = libgfortran3
PKGFILES_CSWlibgfortran3 += $(call baseisadirs,$(libdir),libgfortran\.so\.3(\.\d+)*)
SPKG_DESC_CSWlibgfortran3 += $(DESCRIPTION), libgfortran.so.3
RUNTIME_DEP_PKGS_$(PKG_BASENAME) += CSWlibgfortran3
RUNTIME_DEP_PKGS_CSWlibgfortran3 += CSWlibgcc-s1

PACKAGES += CSWlibgij$(JAVA_LIB_VERSION)
CATALOGNAME_CSWlibgij$(JAVA_LIB_VERSION) = libgij$(JAVA_LIB_VERSION)
PKGFILES_CSWlibgij$(JAVA_LIB_VERSION) += $(call baseisadirs,$(libdir),libgij\.so\.$(JAVA_LIB_VERSION)(\.\d+)*)
SPKG_DESC_CSWlibgij$(JAVA_LIB_VERSION) += $(DESCRIPTION), libgij.so.$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_CSWlibgij$(JAVA_LIB_VERSION) += CSWlibgcj$(JAVA_LIB_VERSION)

PACKAGES += CSWlibgomp1
CATALOGNAME_CSWlibgomp1 = libgomp1
PKGFILES_CSWlibgomp1 += $(call baseisadirs,$(libdir),libgomp\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibgomp1 += $(DESCRIPTION), libgomp.so.1
RUNTIME_DEP_PKGS_CSWlibgomp1 += CSWlibgcc-s1


PACKAGES += CSWlibobjc$(LIBOBJC)
CATALOGNAME_CSWlibobjc$(LIBOBJC) = libobjc$(LIBOBJC)
PKGFILES_CSWlibobjc$(LIBOBJC) += $(call baseisadirs,$(libdir),libobjc\.so\.$(LIBOBJC)(\.\d+)*)
SPKG_DESC_CSWlibobjc$(LIBOBJC) += $(DESCRIPTION), libobjc.so.$(LIBOBJC)
RUNTIME_DEP_PKGS_CSWlibobjc$(LIBOBJC) += CSWlibgcc-s1

PACKAGES += CSWlibobjc-gc$(LIBOBJC)
CATALOGNAME_CSWlibobjc-gc$(LIBOBJC) = libobjc_gc$(LIBOBJC)
PKGFILES_CSWlibobjc-gc$(LIBOBJC) += $(call baseisadirs,$(libdir),libobjc_gc\.so\.$(LIBOBJC)(\.\d+)*)
SPKG_DESC_CSWlibobjc-gc$(LIBOBJC) += $(DESCRIPTION), libobjc_gc.so.$(LIBOBJC)
RUNTIME_DEP_PKGS_CSWlibobjc-gc$(LIBOBJC) += CSWlibgcc-s1

PACKAGES += CSWlibssp0
CATALOGNAME_CSWlibssp0 = libssp0
PKGFILES_CSWlibssp0 += $(call baseisadirs,$(libdir),libssp\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibssp0 += $(DESCRIPTION), libssp.so.0
RUNTIME_DEP_PKGS_CSWlibssp0 += CSWlibgcc-s1

PACKAGES += CSWlibgo0
PKGFILES_CSWlibgo0 += $(call baseisadirs,$(libdir),libgo\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibgo0 += $(DESCRIPTION), libgo.so.0
RUNTIME_DEP_PKGS_CSWlibgo0 += CSWlibgcc-s1
# Hasn't been investigated. I feel lucky.
CHECKPKG_OVERRIDES_CSWlibgo0 += file-with-bad-content

PACKAGES += CSWlibitm1
PKGFILES_CSWlibitm1 += $(call baseisadirs,$(libdir),libitm\.so\.1(\.\d+)*)
SPKG_DESC_CSWlibitm1 += $(DESCRIPTION), libitm.so.1
RUNTIME_DEP_PKGS_CSWlibitm1 += CSWlibgcc-s1

LIBSTDCXX_VERSION = 6

PACKAGES += CSWlibstdc++$(LIBSTDCXX_VERSION)
CATALOGNAME_CSWlibstdc++$(LIBSTDCXX_VERSION) = libstdc++$(LIBSTDCXX_VERSION)
PKGFILES_CSWlibstdc++$(LIBSTDCXX_VERSION) += $(call baseisadirs,$(libdir),libstdc\+\+\.so\.$(LIBSTDCXX_VERSION)(\.\d+)*)
SPKG_DESC_CSWlibstdc++$(LIBSTDCXX_VERSION) += $(DESCRIPTION), libstdc++.so.$(LIBSTDCXX_VERSION)
RUNTIME_DEP_PKGS_CSWlibstdc++$(LIBSTDCXX_VERSION) += CSWlibgcc-s1

# The libquadmath.so.0 library is only build on Intel
PACKAGES_i386 += CSWlibquadmath0
CATALOGNAME_CSWlibquadmath0 = libquadmath0
PKGFILES_CSWlibquadmath0 += $(call baseisadirs,$(libdir),libquadmath\.so\.0(\.\d+)*)
SPKG_DESC_CSWlibquadmath0 += GNU C compiler, libquadmath.so.0
RUNTIME_DEP_PKGS_CSWlibquadmath0 += CSWlibgcc-s1

# Dependencies only on Intel
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core_i386 += CSWlibquadmath0
RUNTIME_DEP_PKGS_CSWlibgfortran3_i386 += CSWlibquadmath0
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += $(RUNTIME_DEP_PKGS_$(PKG_BASENAME)core_$(GARCH))
RUNTIME_DEP_PKGS_CSWlibgfortran3 += $(RUNTIME_DEP_PKGS_CSWlibgfortran3_$(GARCH))

PACKAGES += $(PKG_BASENAME)g++
SPKG_DESC_$(PKG_BASENAME)g++ = GNU C++ Compiler
PKGFILES_$(PKG_BASENAME)g++  = $(foreach F,$(CXX_BINARIES),$(bindir)/$(F)$(PROGRAM_SUFFIX))
PKGFILES_$(PKG_BASENAME)g++ += $(foreach F,$(CXX_BINARIES),$(prefix)/$(PKG_VERSION_TOKEN)/bin/$(F))
PKGFILES_$(PKG_BASENAME)g++ += $(bindir)/\w+-\w+-solaris[\d\.]+-[cg]\+\+$(PROGRAM_SUFFIX)
PKGFILES_$(PKG_BASENAME)g++ += $(libexecdir)/.*cc1plus
PKGFILES_$(PKG_BASENAME)g++ += $(libdir)/.*libstdc.*a
PKGFILES_$(PKG_BASENAME)g++ += $(call baseisadirs,$(libdir),libstdc\+\+\.so)
PKGFILES_$(PKG_BASENAME)g++ += $(mandir)/.*g\+\+.1
# I do not understand this regular expression.
PKGFILES_$(PKG_BASENAME)g++ += $(includedir)/c\+\+/(\d+(?:\.\d+)*)/[a-fA-F,h-iH-I,k-nI-N,p-zP-Z,]+.*
PKGFILES_$(PKG_BASENAME)g++ += $(includedir)/c\+\+/(\d+(?:\.\d+)*)/ostream.*
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += CSWlibcloog-isl2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += CSWlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += CSWlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += CSWlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += CSWlibppl-c4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += CSWlibstdc++$(LIBSTDCXX_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += CSWlibz1

# The C++ compiler needs the C compiler.
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += $(PKG_BASENAME)core

ALTERNATIVES_$(PKG_BASENAME)g++ += $(PKG_VERSION_TOKEN)g++
ALTERNATIVE_$(PKG_VERSION_TOKEN)g++ += $(bindir)/g++ gcc_gplusplus $(bindir)/g++$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)

RUNTIME_DEP_PKGS_CSWlibgij$(JAVA_LIB_VERSION) += CSWlibgcc-s1

PACKAGES += $(PKG_BASENAME)gfortran
SPKG_DESC_$(PKG_BASENAME)gfortran   = GNU Fortran Compiler
PKGFILES_$(PKG_BASENAME)gfortran += $(foreach F,$(FORTRAN_BINARIES),$(bindir)/$(F)$(PROGRAM_SUFFIX))
PKGFILES_$(PKG_BASENAME)gfortran += $(foreach F,$(FORTRAN_BINARIES),$(prefix)/$(PKG_VERSION_TOKEN)/bin/$(F))
PKGFILES_$(PKG_BASENAME)gfortran += $(bindir)/\w+-\w+-solaris[\d\.]+-gfortran$(PROGRAM_SUFFIX)
PKGFILES_$(PKG_BASENAME)gfortran += $(libdir)/.*libgfortran.*a
PKGFILES_$(PKG_BASENAME)gfortran += $(libexecdir)/.*f951
PKGFILES_$(PKG_BASENAME)gfortran += $(mandir)/.*gfortran.1
PKGFILES_$(PKG_BASENAME)gfortran += $(infodir)/gfortran.*
PKGFILES_$(PKG_BASENAME)gfortran += $(call baseisadirs,$(libdir),libgfortran\.so)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += CSWlibcloog-isl2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += CSWlibgfortran3
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += CSWlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += CSWlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += CSWlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += CSWlibppl-c4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += CSWlibz1

ALTERNATIVES_$(PKG_BASENAME)gfortran += gfortran
ALTERNATIVE_gfortran += $(bindir)/gfortran gcc_gfortran $(bindir)/gfortran$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)

PACKAGES += $(PKG_BASENAME)java
SPKG_DESC_$(PKG_BASENAME)java       = GNU Java Compiler
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibcloog-isl2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibgcc-s1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibgcj$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibgcj-tools$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibgij$(JAVA_LIB_VERSION)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWecj
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibppl-c4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibz1
CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += surplus-dependency|CSWecj

PKGFILES_$(PKG_BASENAME)java  = $(foreach F,$(JAVA_BINARIES),$(bindir)/$(F)$(PROGRAM_SUFFIX))
PKGFILES_$(PKG_BASENAME)java += $(foreach F,$(JAVA_BINARIES),$(prefix)/$(PKG_VERSION_TOKEN)/bin/$(F))
PKGFILES_$(PKG_BASENAME)java += $(bindir)/\w+-\w+-solaris[\d\.]+-gcj$(PROGRAM_SUFFIX)
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gcj.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gij.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/jv.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/jcf.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/grmi.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*jar.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*jni.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*java.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gorbd.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gapplet.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gkeytool.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gserialver.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gtnameserv.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gnative2ascii.*
PKGFILES_$(PKG_BASENAME)java += $(mandir)/.*/gc-analyze.*
PKGFILES_$(PKG_BASENAME)java += $(datadir)/java/.*
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*libgij.*a
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*libffi.*a
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*lib-gnu-awt.*a
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*security.*
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*logging.properties
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*pkgconfig.*
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*gcj.*a
PKGFILES_$(PKG_BASENAME)java += $(libdir)/.*libgcj.*a
PKGFILES_$(PKG_BASENAME)java += $(libexecdir)/.*collect.*
PKGFILES_$(PKG_BASENAME)java += $(libexecdir)/.*jvgenmain
PKGFILES_$(PKG_BASENAME)java += $(libexecdir)/.*jc1.*
PKGFILES_$(PKG_BASENAME)java += $(infodir)/gcj.*
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*gcj/.*
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*awt/.*
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*classpath/.*
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*java.*
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*ffi.h
PKGFILES_$(PKG_BASENAME)java += $(includedir)/.*org/.*

# The following list could be probably expanded from $(JAVA_BINARIES)
ALTERNATIVES_$(PKG_BASENAME)java += $(PKG_VERSION_TOKEN)java
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/aot-compile gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX) $(ALTERNATIVES_PRIO)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gappletviewer gcc_gjava $(bindir)/gappletviewer$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gc-analyze gcc_gjava $(bindir)/gc-analyze$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gcj gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gcj-dbtool gcc_gjava $(bindir)/gcj-dbtool$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gcjh gcc_gjava $(bindir)/gcjh$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gij gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gjar gcc_gjava $(bindir)/gjar$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gjarsigner gcc_gjava $(bindir)/gjarsigner$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gjavah gcc_gjava $(bindir)/gjavah$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gkeytool gcc_gjava $(bindir)/gkeytool$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gnative2ascii gcc_gjava $(bindir)/$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gorbd gcc_gjava $(bindir)/gorbd$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/grmic gcc_gjava $(bindir)/grmic$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/grmid gcc_gjava $(bindir)/grmid$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/grmregistry gcc_gjava $(bindir)/grmregistry$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/grmregistry gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gserialver gcc_gjava $(bindir)/gserialver$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/gtnameserv gcc_gjava $(bindir)/gtnameserv$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/jcf-dump gcc_gjava $(bindir)/jcf-dump$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/jv-convert gcc_gjava $(bindir)/jv-convert$(PROGRAM_SUFFIX)
ALTERNATIVE_$(PKG_VERSION_TOKEN)java += $(bindir)/rebuild-gcj-db gcc_gjava $(bindir)/rebuild-gcj-db$(PROGRAM_SUFFIX)

PACKAGES += $(PKG_BASENAME)objc
SPKG_DESC_$(PKG_BASENAME)objc       = GNU Objective C Compiler
PKGFILES_$(PKG_BASENAME)objc  = $(libexecdir)/.*cc1obj
PKGFILES_$(PKG_BASENAME)objc += $(libdir)/.*libobjc.*a
PKGFILES_$(PKG_BASENAME)objc += $(includedir)/.*objc/.*
PKGFILES_$(PKG_BASENAME)objc += $(libdir)/.*/include/objc/.*
PKGFILES_$(PKG_BASENAME)objc += $(call baseisadirs,$(libdir),libobjc.so)
PKGFILES_$(PKG_BASENAME)objc += $(call baseisadirs,$(libdir),libobjc_gc.so)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += CSWlibcloog-isl2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += CSWlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += CSWlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += CSWlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += CSWlibobjc$(LIBOBJC)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += CSWlibobjc-gc$(LIBOBJC)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += CSWlibppl-c4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += CSWlibz1

# libiconv deps cropped up relatively late in the porting process. Perhaps
# they apply to all arch/OS combinations.
RUNTIME_DEP_PKGS_$(PKG_BASENAME)core += CSWlibiconv2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)g++ += CSWlibiconv2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)gfortran += CSWlibiconv2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)java += CSWlibiconv2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)objc += CSWlibiconv2

PACKAGES += $(PKG_BASENAME)ada
SPKG_DESC_$(PKG_BASENAME)ada       = GCC Ada compiler (GNAT)
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada         = $(PKG_BASENAME)core
PKGFILES_$(PKG_BASENAME)ada  = $(prefix)/libexec/.*gnat1
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/lib/.*libgnat.*a
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/lib/.*libgnarl.*a
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/.*/adalib/.*
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/.*/adainclude/.*
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/info/.*gnat.*
PKGFILES_$(PKG_BASENAME)ada += $(prefix)/bin/gnat(?!ive).*
# There are static libraries, .a files in the ada package. Let them be.
CHECKPKG_OVERRIDES_$(PKG_BASENAME)ada += discouraged-path-in-pkgmap
# It needs the core compiler.
CHECKPKG_OVERRIDES_$(PKG_BASENAME)ada += surplus-dependency|$(PKG_BASENAME)core
CHECKPKG_OVERRIDES_$(PKG_BASENAME)ada += file-with-bad-content

RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += CSWlibcloog-isl2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += CSWlibgcc-s1
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += CSWlibgmp10
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += CSWlibiconv2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += CSWlibmpc2
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += CSWlibmpfr4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += CSWlibppl-c4
RUNTIME_DEP_PKGS_$(PKG_BASENAME)ada += CSWlibz1

# This is an obsolete package. Nothing depends on it, so we can remove it.
INCOMPATIBLE_PKGS_$(PKG_BASENAME)ada = $(PKG_BASENAME)adart

PACKAGES += $(PACKAGES_$(GARCH))
CORE_BINARIES = cpp gcc gcov
CXX_BINARIES = g\+\+ c\+\+
FORTRAN_BINARIES = gfortran
JAVA_BINARIES  = gcj gij aot-compile grmiregistry
JAVA_BINARIES += gappletviewer gc-analyze gcj-dbtool gcjh gjar gjarsigner gjavah
JAVA_BINARIES += gkeytool gnative2ascii gorbd grmic grmid grmregistry
JAVA_BINARIES += gserialver gtnameserv jcf-dump jv-convert rebuild-gcj-db

# GCC-4.7 contains assembler specific to sparcv9, incompatible with sparcv8.
# If we wanted to build it on Solaris 9, we would have to add these overrides.
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)ada += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)core += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)g++ += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)gfortran += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)java += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_$(PKG_BASENAME)objc += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibffi4 += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibgcc-s1 += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibgcj$(JAVA_LIB_VERSION) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibgcj-tools$(JAVA_LIB_VERSION) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibgfortran3 += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibgij$(JAVA_LIB_VERSION) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlib-gnu-awt-xlib$(JAVA_LIB_VERSION) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibgomp1 += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibobjc$(LIBOBJC) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibobjc-gc$(LIBOBJC) += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibssp0 += binary-architecture-does-not-match-placement
# CHECKPKG_OVERRIDES_CSWlibstdc++6 += binary-architecture-does-not-match-placement

# We're building with the default GAR maps, currently U5.
# LINKER_MAP_RELEASE = solaris10u8

#Direct binding is disabled to to problem with amd64 libs
CHECKPKG_OVERRIDES_CSWgcc4java += no-direct-binding
CHECKPKG_OVERRIDES_CSWgcc4core += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibgij13 += no-direct-binding
CHECKPKG_OVERRIDES_CSWgcc4g++ += no-direct-binding
CHECKPKG_OVERRIDES_CSWgcc4ada += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibgcj13 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibgo0 += no-direct-binding
CHECKPKG_OVERRIDES_CSWgcc4gfortran += no-direct-binding
CHECKPKG_OVERRIDES_CSWgcc4objc += no-direct-binding
CHECKPKG_OVERRIDES_CSWlib-gnu-awt-xlib13 += soname-unused
CHECKPKG_OVERRIDES_CSWlib-gnu-awt-xlib13 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibgcj-tools13 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibgfortran3 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibobjc4 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibstdc++6 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibitm1 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibffi4 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibobjc-gc4 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibquadmath0 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibssp0 += no-direct-binding
CHECKPKG_OVERRIDES_CSWlibgomp1 += no-direct-binding


include files/scripts.mk
include gar/category.mk

post-install-modulated:
	ginstall -d -m 755 $(DESTDIR)$(prefix)/$(PKG_VERSION_TOKEN)/bin
	for b in $(CORE_BINARIES) $(CXX_BINARIES) \
		$(FORTRAN_BINARIES) $(JAVA_BINARIES); do \
		gln -v -s -f ../../bin/$${b}$(PROGRAM_SUFFIX) \
		$(DESTDIR)$(prefix)/$(PKG_VERSION_TOKEN)/bin/$${b}; \
	done
	bash $(FILEDIR)/customize_specs.sh $(DESTDIR) $(PROGRAM_SUFFIX) $(VERSION)
	@$(MAKECOOKIE)

# Use CSW or Solaris tools explicitly:
AR = /usr/ccs/bin/ar
AS = /usr/ccs/bin/as
NM = /usr/ccs/bin/nm
RANLIB = /usr/ccs/bin/ranlib
STRIP = /usr/css/bin/strip
OBJCOPY = /opt/csw/bin/gobjcopy
OBJDUMP = /opt/csw/bin/gobjdump
READELF = /opt/csw/bin/greadelf

CONFIGURE_ENV := PATH=$(PATH) CC=$(CC) LD_OPTIONS="$(LD_OPTIONS)" AR=$(AR) AS=$(AS) NM=$(NM) RANLIB=$(RANLIB) STRIP=$(STRIP) OBJCOPY=$(OBJCOPY) OBJDUMP=$(OBJDUMP) READELF=$(READELF)
BUILD_ENV := PATH=$(PATH) LD_OPTIONS="$(LD_OPTIONS)" AR=$(AR) AS=$(AS) NM=$(NM) RANLIB=$(RANLIB) STRIP=$(STRIP) OBJCOPY=$(OBJCOPY) OBJDUMP=$(OBJDUMP) READELF=$(READELF)
INSTALL_ENV := PATH=$(PATH) AR=$(AR) AS=$(AS) NM=$(NM) RANLIB=$(RANLIB) STRIP=$(STRIP) OBJCOPY=$(OBJCOPY) OBJDUMP=$(OBJDUMP) READELF=$(READELF)
