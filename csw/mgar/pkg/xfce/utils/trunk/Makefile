NAME = xfce-utils
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Utilities
define BLURB
   Xfce Utilities 
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
DISTFILES += CSWxfceutils.depend CSWxfceutils.gspec CSWxfceutils.prototype
DISTFILES += CSWxfceutilsdoc.depend CSWxfceutilsdoc.gspec CSWxfceutilsdoc.prototype

# PATCHFILES = xinitrc.patch

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

CPPFLAGS += -I$(DESTDIR)/opt/csw/include/dbus-1.0
CPPFLAGS += -I$(DESTDIR)/opt/csw/lib/dbus-1.0/include

CONFIGURE_ARGS += --enable-dbus

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )

