NAME = mibdump
VERSION = 0.1.2
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = Allows management applications to access SMI MIB module definitions
define BLURB
  The core of the libsmi distribution is a library that allows management applications
  to access SMI MIB module definitions. On top of this library, there are tools to check,
  analyze dump, convert, and compare MIB definitions. Finally, the distribution contains
  a steadily maintained and revised archive of all IETF and IANA maintained standard MIB
  and PIB modules.
endef

MASTER_SITES = ftp://ftp.ibr.cs.tu-bs.de/pub/local/libsmi/
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.ibr.cs.tu-bs.de/projects/libsmi/

RUNTIME_DEP_PKGS = CSWlibsmi

BUILD64_LIBS_ONLY = 1
CONFIGURE_ARGS = $(DIRPATHS)

include gar/category.mk
