NAME = mod_ruby
VERSION = 1.2.4
GARTYPE = v1
CATEGORIES = server

DESCRIPTION = an Apache/Ruby integration module
define BLURB
  mod_ruby is an Apache module that embeds the Ruby language interpreter
  within the server, allowing for Apache handlers to be written in Ruby for
  faster and more powerful applications than plain CGI.
endef

MASTER_SITES = http://www.modruby.net/archive/
DISTFILES  = $(NAME)-$(VERSION).tar.gz
DISTFILES += CSWap2modruby.gspec
#DISTFILES += CSWap2modruby.depend
#DISTFILES += CSWap2modruby.prototype
#DISTFILES += CSWap2modruby.postinstall
#DISTFILES += CSWap2modruby.preremove
#DISTFILES += CSWap2modruby.space

# We define upstream file regex so we can be notifed of new upstream software release
UFILES_REGEX = $(NAME)-(\d+(?:\.\d+)*).tar.gz

CONFIGURE_SCRIPTS = ruby

CONFIGURE_ARGS  = --prefix=$(prefix)
CONFIGURE_ARGS += --mandir=$(mandir)
CONFIGURE_ARGS += --with-apxs=$(prefix)/apache2/sbin/apxs
CONFIGURE_ARGS += --with-apr-includes=$(shell apr-config --includedir)

include gar/category.mk

configure-ruby:
	( cd $(WORKSRC) ; \
		$(CONFIGURE_ENV) ./configure.rb $(CONFIGURE_ARGS) )
	@$(MAKECOOKIE)
