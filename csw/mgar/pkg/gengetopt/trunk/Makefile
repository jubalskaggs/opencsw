NAME = gengetopt
VERSION = 2.22.4
CATEGORIES = utils
GARTYPE = v2

DESCRIPTION = parses the command line options
define BLURB
	'getgetopt' takes an easy-to-do description of options and generates a C
	function that uses the GNU getopt_long(3) function to parse and validate the
	options. gengetopt is perfect if you don't want to write all the stuff
	required to call GNU getopt_long(3), or if you have a program and wish it
	took many options. The generated code works if you use autoconf or automake.
endef

MASTER_SITES = $(GNU_MIRROR)
DISTFILES  = $(NAME)-$(VERSION).tar.gz

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

SPKG_SOURCEURL = http://www.gnu.org/software/gengetopt/

BUILD64_LIBS_ONLY = 1

CONFIGURE_ARGS = $(DIRPATHS) 

TEST_SCRIPTS =

include gar/category.mk
