NAME = xfce4-panel
GARTYPE = v1
CATEGORIES = xfce

DESCRIPTION = Xfce Panel
define BLURB
   Xfce Panel 
endef

DISTFILES  = $(NAME)-$(VERSION).tar.bz2
# DISTFILES += CSWxfcepaneldoc.depend CSWxfcepaneldoc.gspec CSWxfcepaneldoc.prototype
# DISTFILES += CSWlibxfcepaneldev.depend CSWlibxfcepaneldev.gspec CSWlibxfcepaneldev.prototype
# DISTFILES += CSWlibxfcepanel.depend CSWlibxfcepanel.gspec CSWlibxfcepanel.prototype
# DISTFILES += CSWxfcepanel.depend CSWxfcepanel.gspec CSWxfcepanel.prototype

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.bz2

DISTFILES += $(call admfiles,CSWxfcepanel, depend)

TEST_SCRIPTS = none

include gar/category.mk

test-none :
	@$(MAKECOOKIE)

post-install:
	( gfind $(DESTDIR)/opt/csw -exec bash -c "file {} | ggrep ELF | ggrep -e 'executable' -e 'dynamic lib' | ggrep 'not stripped' && strip {}"  \; )
