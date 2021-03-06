# $Id$

# TODO
# - One big "mta" switch in alternatives between sendmail/postfix

# + Build separate 9/10 packages? -> build only 5.10
# + add symlink from /etc/opt/csw/mail/cf to /opt/csw/share/sendmail/cf/cf
# + add ostype solaris9csw.m4
# + add sendmail.mc in cf dir
# + /opt/csw/lib/sendmail 2555 root smmsp (Rafael Ostertag)
# + remove statistics
# + csw-sm-client.pid, csw-sendmail.pid
# + smmsp:smmsp /var/opt/csw/spool/clientmqueue
# + Include Makefile in /etc/opt/csw/mail
# + post message
# + Fix paths in sendmail.cf and cswsendmail
# + #4486 Provide sendmail's contrib/ tools as a separate package?
# + Include activate/deactivate scripts
# + migrate conf from /opt/csw/etc/mail
# + Tests? Not really possible to test during build
# + build libmilter
# + use alternatives to clear collisions with postfix, see sudo as example
# + never start cswsendmail by default (collides with system sendmail)
# + path to sendmail.cf (/etc/opt/csw/mail)
# + bdb hash support
# + cpsample conf files
# + remove COPYING file
# + copy usergroup file into place
# + #3864 Sendmail must be relinked with new berkeley db -> bdb48
# + #2915 Must stop built-in sendmail manually -> n/a
# + #4150 Sendmail 8.14.4 released -> this is 8.14.5

NAME = sendmail
VERSION = 8.15.1
GARTYPE = v2

DESCRIPTION = Sendmail MTA
define BLURBBLURB
  Sendmail MTA
endef

MASTER_SITES = ftp://ftp.sendmail.org/pub/sendmail/
SPKG_SOURCEURL = http://www.sendmail.org

DISTFILES  = $(NAME).$(VERSION).tar.gz
DISTFILES += aliases helpfile local-host-names sendmail.cf
DISTFILES += submit.cf trusted-users
DISTFILES += README.CSW sendmail.schema site.config.m4
DISTFILES += oracle-sendmail-deactivate.sh oracle-sendmail-reactivate.sh
DISTFILES += cswsendmail cswusergroup
DISTFILES += sendmail.mc solaris9csw.m4

LICENING_PLATFORMS = solaris10-sparc solaris10-i3864

LICENSE = LICENSE

PACKAGES                      = CSWsendmail 
CATALOGNAME_CSWsendmail       = sendmail
SPKG_DESC_CSWsendmail         = $(DESCRIPTION)
RUNTIME_DEP_PKGS_CSWsendmail += CSWbdb48
RUNTIME_DEP_PKGS_CSWsendmail += CSWlibwrap1
RUNTIME_DEP_PKGS_CSWsendmail += CSWlibssl1-0-0
RUNTIME_DEP_PKGS_CSWsendmail += CSWlibsasl2-2
RUNTIME_DEP_PKGS_CSWsendmail += CSWliblber2-4-2
RUNTIME_DEP_PKGS_CSWsendmail += CSWlibldap2-4-2

PACKAGES                += CSWlibmilter 
CATALOGNAME_CSWlibmilter = libmilter
SPKG_DESC_CSWlibmilter   = Sendmail MTA milter
PKGFILES_CSWlibmilter    = $(docdir)/libmilter/.*
PKGFILES_CSWlibmilter   += /opt/csw/include/libmilter.h
PKGFILES_CSWlibmilter   += /opt/csw/include/libmilter/mfapi.h
PKGFILES_CSWlibmilter   += /opt/csw/include/libmilter/mfdef.h
PKGFILES_CSWlibmilter   += /opt/csw/include/libsmdb/smdb.h
PKGFILES_CSWlibmilter   += $(libdir)/libmilter.a
PKGFILES_CSWlibmilter   += $(libdir)/libsm.a
PKGFILES_CSWlibmilter   += $(libdir)/libsmdb.a
PKGFILES_CSWlibmilter   += $(libdir)/libsmutil.a

PACKAGES                            += CSWsendmail-contrib 
CATALOGNAME_CSWsendmail-contrib      = sendmail_contrib
SPKG_DESC_CSWsendmail-contrib        = Sendmail MTA contrib
RUNTIME_DEP_PKGS_CSWsendmail-contrib = CSWperl
ARCHALL_CSWsendmail-contrib          = 1
PKGFILES_CSWsendmail-contrib         = $(docdir)/sendmail_contrib/.*
PKGFILES_CSWsendmail-contrib        += $(bindir)/link_hash.sh
PKGFILES_CSWsendmail-contrib        += $(bindir)/movemail.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/smcontrol.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/passwd-to-alias.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/socketmapClient.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/bounce-resender.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/doublebounce.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/mailprio
PKGFILES_CSWsendmail-contrib        += $(bindir)/socketmapServer.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/qtool.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/buildvirtuser
PKGFILES_CSWsendmail-contrib        += $(bindir)/etrn.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/re-mqueue.pl
PKGFILES_CSWsendmail-contrib        += $(bindir)/cidrexpand
PKGFILES_CSWsendmail-contrib        += $(bindir)/expn.pl
PKGFILES_CSWsendmail-contrib        += $(mandir)/man1/etrn.0
PKGFILES_CSWsendmail-contrib        += $(mandir)/man8/qtool.8
PKGFILES_CSWsendmail-contrib        += $(sysconfdir)/movemail.conf

INITSMF     = /etc/opt/csw/init.d/cswsendmail
SAMPLECONF  = $(addprefix /etc/opt/csw/mail/,$(CONFFILES))
USERGROUP   = /etc/opt/csw/pkg/CSWsendmail/cswusergroup
POSTMSG     = $(docdir)/sendmail/README.postinstall

# Enable support for files > 2GB in size.
EXTRA_CFLAGS = -D_FILE_OFFSET_BITS=64 -D_LARGEFILE_SOURCE

# Do not remove the static libs from libmilter
MERGE_EXCLUDE_STATICLIBS =

# Patches
PATCHFILES += 0001-add-libmilter-to-the-Makefile.patch
PATCHFILES += 0002-no-gnuism.patch
PATCHFILES += 0003-fix-Makefile-in-cf-dir.patch

MIGRATE_FILES_CSWsendmail      = aliases helpfile local-host-names sendmail.cf
MIGRATE_FILES_CSWsendmail     += submit.cf trusted-users
MIGRATE_SOURCE_DIR_CSWsendmail = /opt/csw/etc/mail
MIGRATE_DEST_DIR_CSWsendmail   = /etc/opt/csw/mail

PROTOTYPE_MODIFIERS = 1 2
PROTOTYPE_FILES_1   = /var/opt/csw/spool/clientmqueue
PROTOTYPE_USER_1    = smmsp
PROTOTYPE_GROUP_1   = smmsp
PROTOTYPE_PERMS_1   = 0770
PROTOTYPE_FILES_2   = /opt/csw/lib/sendmail
PROTOTYPE_USER_2    = root
PROTOTYPE_GROUP_2   = smmsp
PROTOTYPE_PERMS_2   = 2555

CONFIGURE_SCRIPTS   = custom
BUILD_SCRIPTS       = custom
TEST_SCRIPTS        = custom
INSTALL_SCRIPTS     = custom

# Some files collide with CSWpostfix
ALTERNATIVES_CSWsendmail  = sendmail
ALTERNATIVE_sendmail  = $(bindir)/mailq sendmail $(bindir)/mailq.sendmail 100
ALTERNATIVE_sendmail += $(bindir)/newaliases newaliases $(bindir)/newaliases.sendmail
ALTERNATIVE_sendmail += $(mandir)/man1/mailq.1 mailq.1 $(mandir)/man1/mailq1.1.sendmail
ALTERNATIVE_sendmail += $(mandir)/man1/newaliases.1 newaliases.1 $(mandir)/man1/newaliases.1.sendmail
ALTERNATIVE_sendmail += $(mandir)/man5/aliases.5 aliases.5 $(mandir)/man5/REINPLACE_USRLOCAL += $(sysconfdir)/movemail.conf
REINPLACE_USRLOCAL += $(bindir)/bounce-resender.pl
REINPLACE_USRLOCAL += $(bindir)/movemail.pl
REINPLACE_USRLOCAL += $(bindir)/doublebounce.pl
REINPLACE_USRLOCAL += $(bindir)/re-mqueue.pl
REINPLACE_USRLOCAL += $(bindir)/expn.pl
REINPLACE_WHEN_USRLOCAL = postinstall

# Don't know how to fix this or if it needs fixing
CHECKPKG_OVERRIDES_CSWsendmail += no-direct-bindinge/sendmail/cf/README

# The static libs from libmilter
CHECKPKG_OVERRIDES_CSWlibmilter += discouraged-path-in-pkgmap|/opt/csw/lib/libsmutil.a
CHECKPKG_OVERRIDES_CSWlibmilter += discouraged-path-in-pkgmap|/opt/csw/lib/libmilter.a
CHECKPKG_OVERRIDES_CSWlibmilter += discouraged-path-in-pkgmap|/opt/csw/lib/libsm.a
CHECKPKG_OVERRIDES_CSWlibmilter += discouraged-path-in-pkgmap|/opt/csw/lib/libsmdb.a

include gar/category.mk

PLATFORM  = $(shell if [ `uname -i` = "i86pc" ] ; then echo i86pc ; else echo sun4 ; fi )
OBJDIR    = $(WORKDIR)/$(DISTNAME)/obj.SunOS.$(GAROSREL).$(PLATFORM)
LIBFILES  = sendmail/sendmail mail.local/mail.local smrsh/smrsh rmail/rmail
LIBMILTER = libmilter/libmilter.a libsm/libsm.a libsmdb/libsmdb.a libsmutil/libsmutil.a
BINFILES  = vacation/vacation
SBINFILES = makemap/makemap editmap/editmap praliases/praliases \
            mailstats/mailstats
MANFILES1 = sendmail/mailq.1 sendmail/newaliases.1 vacation/vacation.1
MANFILES5 = sendmail/aliases.5
MANFILES8 = sendmail/sendmail.8 mailstats/mailstats.8 makemap/makemap.8 \
            praliases/praliases.8 smrsh/smrsh.8 mail.local/mail.local.8 \
            rmail/rmail.8 editmap/editmap.8
CONFFILES = aliases helpfile local-host-names sendmail.cf \
            submit.cf trusted-users
INCLFILES = libmilter/libmilter.h
CONTBIN   = link_hash.sh movemail.pl smcontrol.pl \
            passwd-to-alias.pl socketmapClient.pl bounce-resender.pl \
            doublebounce.pl mailprio socketmapServer.pl \
            qtool.pl buildvirtuser etrn.pl re-mqueue.pl \
            cidrexpand expn.pl
CONTDOC   = dnsblaccess.m4 domainmap.m4 mmuegel
CONTMAN1  = etrn.0
CONTMAN8  = qtool.8
CONTCONF  = movemail.conf

configure-custom:
	@echo " ==> Configuring $(NAME) (custom)"
	@( gsed 's,%CFLAGS%,$(CFLAGS),;s,%OCSWCC%,$(CC),' \
		$(DOWNLOADDIR)/site.config.m4 > \
		$(WORKSRC)/devtools/Site/site.config.m4 )
	@$(MAKECOOKIE)

build-custom:
	@echo " ==> Building $(NAME) (custom)PATH=/opt/csw/gnu:/opt/csw/bin:/bin)"
	cd $(WORKSRC) && ./Build
	@$(MAKECOOKIE)

test-custom:
	@echo " ==> Testing $(NAME) (custom)"
	@$(MAKECOOKIE)

install-custom:
	@echo " ==> Installing $(NAME) (custom)"

	@# Install dirs
	ginstall -d $(DESTDIR)$(libdir)
	ginstall -d $(DESTDIR)$(bindir)
	ginstall -d $(DESTDIR)$(sbindir)
	ginstall -d $(DESTDIR)$(mandir)/man1
	ginstall -d $(DESTDIR)$(mandir)/man5
	ginstall -d $(DESTDIR)$(mandir)/man8
	ginstall -d $(DESTDIR)/var/opt/csw/spool/clientmqueue
	ginstall -d $(DESTDIR)$(sharedstatedir)/sendmail
	ginstall -d $(DESTDIR)/etc/opt/csw/init.d
	ginstall -d $(DESTDIR)$(sysconfdir)/mail
	ginstall -d $(DESTDIR)/opt/csw/include
	ginstall -d $(DESTDIR)/opt/csw/include/libmilter
	ginstall -d $(DESTDIR)/opt/csw/include/libsmdb
	ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)
	ginstall -m 755 -d $(DESTDIR)$(docdir)/$(NAME)_contrib
	ginstall -m 755 -d $(DESTDIR)$(docdir)/libmilter
	ginstall -m 755 -d $(DESTDIR)/etc/opt/csw/pkg/CSWsendmail

	@# Install the libraries
	( for file in $(LIBFILES) ; do \
		ginstall -c -m 755 $(OBJDIR)/$$file $(DESTDIR)$(libdir) ; \
		done )

	@# Install the binaries
	ginstall -m 755 $(OBJDIR)/$(BINFILES) $(DESTDIR)$(bindir)
	( for file in $(SBINFILES) ; do \
		ginstall -m 755 $(OBJDIR)/$$file $(DESTDIR)$(sbindir) ; \
		done )

	@# Install manpages
	( for file in $(MANFILES1) ; do \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/man1 ; \
		done )
	( for file in $(MANFILES5) ; do \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/man5 ; \
		done )
	( for file in $(MANFILES8) ; do \
		ginstall -m 644 $(OBJDIR)/$$file $(DESTDIR)$(mandir)/man8 ; \
		done )

	@# Install milter lib files
	( for file in $(LIBMILTER) ; do \
		ginstall -m 444 $(OBJDIR)/$$file $(DESTDIR)$(libdir) ; \
		done )

	@# Install include files
	( for file in $(INCLFILES) ; do \
		ginstall -m 444 $(OBJDIR)/$$file $(DESTDIR)/opt/csw/include ; \
		done )

	@# Install milter files
	ginstall -m 444 $(WORKSRC)/include/libsmdb/smdb.h $(DESTDIR)/opt/csw/include/libsmdb ; \
	ginstall -m 444 $(WORKSRC)/include/libmilter/mfapi.h $(DESTDIR)/opt/csw/include/libmilter ; \
	ginstall -m 444 $(WORKSRC)/include/libmilter/mfdef.h $(DESTDIR)/opt/csw/include/libmilter ; \

	@# Install m4/cf macros
	find $(WORKSRC)/cf -type f -exec chmod 644 {} +
	cp -r $(WORKSRC)/cf $(DESTDIR)$(sharedstatedir)/sendmail
	cp -p $(DOWNLOADDIR)/sendmail.mc $(DESTDIR)$(sharedstatedir)/sendmail/cf/cf/
	cp -p $(DOWNLOADDIR)/solaris9csw.m4 $(DESTDIR)$(sharedstatedir)/sendmail/cf/ostype/

	@# Install startup script
	chmod +x $(DOWNLOADDIR)/cswsendmail && \
		cp -p $(DOWNLOADDIR)/cswsendmail $(DESTDIR)/etc/opt/csw/init.d

	@# Install configurations, XXX missing submit.cf/sendmail.cf
	( for file in $(CONFFILES) ; do \
		ginstall -m 644 $(DOWNLOADDIR)/$$file \
		$(DESTDIR)$(sysconfdir)/mail/$$file; \
		done )
	ln -s $(sharedstatedir)/sendmail/cf/cf $(DESTDIR)$(sysconfdir)/mail/cf

	@# usergroup
	ginstall -m 444 $(FILEDIR)/cswusergroup $(DESTDIR)/etc/opt/csw/pkg/CSWsendmail/

	@# README
	ginstall -m 644 $(FILEDIR)/README.CSW $(DESTDIR)$(docdir)/$(NAME)/

	@# Create links in bindir
	ln -s $(libdir)/sendmail $(DESTDIR)$(bindir)/newaliases
	ln -s $(libdir)/sendmail $(DESTDIR)$(bindir)/mailq
	ln -s $(libdir)/sendmail $(DESTDIR)$(bindir)/purgestats
	ln -s $(libdir)/sendmail $(DESTDIR)$(bindir)/hoststat

	@# Fix alternatives files
	mv $(DESTDIR)$(bindir)/mailq $(DESTDIR)$(bindir)/mailq.sendmail
	mv $(DESTDIR)$(bindir)/newaliases $(DESTDIR)$(bindir)/newaliases.sendmail
	mv $(DESTDIR)$(mandir)/man1/mailq.1 $(DESTDIR)$(mandir)/man1/mailq1.1.sendmail
	mv $(DESTDIR)$(mandir)/man1/newaliases.1 $(DESTDIR)$(mandir)/man1/newaliases.1.sendmail
	mv $(DESTDIR)$(mandir)/man5/aliases.5 $(DESTDIR)$(mandir)/man5/aliases.5.sendmail

	@# Post install message
	ginstall -m 444 $(FILEDIR)/CSWsendmail.postmsg $(DESTDIR)$(docdir)/sendmail/README.postinstall

	@# Milter doc files
	ginstall -m 644 $(WORKSRC)/libmilter/docs/* $(DESTDIR)$(docdir)/libmilter

	@# Contrib files
	( for file in $(CONTBIN) ; do \
		ginstall -m 755 $(WORKSRC)/contrib/$$file $(DESTDIR)$(bindir) ; \
		done )
	( for file in $(CONTCONF) ; do \
		ginstall -m 644 $(WORKSRC)/contrib/$$file $(DESTDIR)$(sysconfdir) ; \
		done )
	( for file in $(CONTDOC) ; do \
		ginstall -m 444 $(WORKSRC)/contrib/$$file $(DESTDIR)$(docdir)/sendmail_contrib ; \
		done )
	( for file in $(CONTMAN1) ; do \
		ginstall -m 644 $(WORKSRC)/contrib/$$file $(DESTDIR)$(mandir)/man1 ; \
		done )
	( for file in $(CONTMAN8) ; do \
		ginstall -m 644 $(WORKSRC)/contrib/$$file $(DESTDIR)$(mandir)/man8 ; \
		done )

	@# Deactivate/reactivate scripts
	ginstall -m 755 $(DOWNLOADDIR)/oracle-sendmail-deactivate.sh $(DESTDIR)$(docdir)/sendmail
	ginstall -m 755 $(DOWNLOADDIR)/oracle-sendmail-reactivate.sh $(DESTDIR)$(docdir)/sendmail

	@# Makefile for databases
	ginstall -m 644 $(FILEDIR)/CSWsendmail.Makefile $(DESTDIR)$(sysconfdir)/mail/Makefi