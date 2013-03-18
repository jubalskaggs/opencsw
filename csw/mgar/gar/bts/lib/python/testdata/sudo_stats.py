import datetime
pkgstats = [{'bad_paths': {},
  'basic_stats': {'catalogname': 'sudo_common',
                  'md5_sum': '2b3bb1d2a9190b5d1813562fb2d1472a',
                  'parsed_basename': {'arch': 'sparc',
                                      'catalogname': 'sudo_common',
                                      'full_version_string': '1.7.2p5,REV=2010.03.02',
                                      'osrel': 'SunOS5.8',
                                      'revision_info': {'REV': '2010.03.02'},
                                      'vendortag': 'CSW',
                                      'version': '1.7.2p5',
                                      'version_info': {'major version': '1',
                                                       'minor version': '7',
                                                       'patchlevel': '2p5'}},
                  'pkg_basename': 'sudo_common-1.7.2p5,REV=2010.03.02-SunOS5.8-sparc-CSW.pkg.gz',
                  'pkg_path': '/tmp/pkg_4nepTE/sudo_common-1.7.2p5,REV=2010.03.02-SunOS5.8-sparc-CSW.pkg.gz',
                  'pkgname': 'CSWsudo-common',
                  'stats_version': 9L},
  'binaries': ['opt/csw/libexec/sudo_noexec.so', 'opt/csw/sbin/visudo'],
  'binaries_dump_info': [{'RPATH set': True,
                          'RUNPATH RPATH the same': True,
                          'RUNPATH set': True,
                          'base_name': 'sudo_noexec.so',
                          'needed sonames': ('libc.so.1',),
                          'path': 'opt/csw/libexec/sudo_noexec.so',
                          'runpath': ('/opt/csw/lib/$ISALIST',
                                      '/opt/csw/lib'),
                          'soname': 'sudo_noexec.so'},
                         {'RPATH set': True,
                          'RUNPATH RPATH the same': True,
                          'RUNPATH set': True,
                          'base_name': 'visudo',
                          'needed sonames': ('libintl.so.8',
                                             'libsocket.so.1',
                                             'libnsl.so.1',
                                             'libc.so.1'),
                          'path': 'opt/csw/sbin/visudo',
                          'runpath': ('/opt/csw/lib/$ISALIST',
                                      '/opt/csw/lib')}],
  'depends': [('CSWcommon',
               'CSWcommon common - common files and dirs for CSW packages '),
              ('CSWggettextrt',
               'CSWggettextrt ggettextrt - GNU locale utilities ')],
  'files_metadata': [{'endian': 'Big endian',
                      'machine_id': 2,
                      'mime_type': 'application/x-executable; charset=binary',
                      'mime_type_by_hachoir': u'application/x-executable',
                      'path': 'opt/csw/sbin/visudo'},
                     {'mime_type': 'text/plain; charset=us-ascii',
                      'path': 'opt/csw/share/doc/sudo_common/license'},
                     {'mime_type': 'text/troff; charset=us-ascii',
                      'path': 'opt/csw/share/man/man4/sudoers.4'},
                     {'mime_type': 'text/troff; charset=us-ascii',
                      'path': 'opt/csw/share/man/man1m/sudo.1m'},
                     {'mime_type': 'text/troff; charset=us-ascii',
                      'path': 'opt/csw/share/man/man1m/visudo.1m'},
                     {'endian': 'Big endian',
                      'machine_id': 2,
                      'mime_type': 'application/x-sharedlib; charset=binary',
                      'mime_type_by_hachoir': u'application/x-executable',
                      'path': 'opt/csw/libexec/sudo_noexec.so'},
                     {'mime_type': 'text/plain; charset=us-ascii',
                      'path': 'opt/csw/etc/sudoers.CSW'}],
  'isalist': ('sparcv9+vis2',
              'sparcv9+vis',
              'sparcv9',
              'sparcv8plus+vis2',
              'sparcv8plus+vis',
              'sparcv8plus',
              'sparcv8',
              'sparcv8-fsmuld',
              'sparcv7',
              'sparc'),
  'ldd_info': {
      'opt/csw/libexec/sudo_noexec.so': [],
      'opt/csw/sbin/visudo': [],
  },
  'binaries_elf_info': {'opt/csw/libexec/sudo_noexec.so': {
    'version needed': [],
    'version definition': [],
    'symbol table': [
      { 'soname': 'libc.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' } ],
    },
    'opt/csw/sbin/visudo': {
      'version definition': [],
      'version needed': [],
      'symbol table': [
        { 'soname': 'libintl.so.8', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
        { 'soname': 'libsocket.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
        { 'soname': 'libnsl.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
        { 'soname': 'libc.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
      ],
    }
  },
  'mtime': datetime.datetime(2010, 3, 2, 22, 34, 40),
  'overrides': [],
  'pkgchk': {'return_code': 0,
             'stderr_lines': ['rm: Cannot remove any directory in the path of the current working directory',
                              '/var/tmp/aaajqaOvt/CSWsudo-common'],
             'stdout_lines': ['Checking uninstalled stream format package <CSWsudo-common> from </tmp/pkg_4nepTE/sudo_common-1.7.2p5,REV=2010.03.02-SunOS5.8-sparc-CSW.pkg>',
                              '## Checking control scripts.',
                              '## Checking package objects.',
                              '## Checking is complete.']},
  'pkginfo': {'ARCH': 'sparc',
              'CATEGORY': 'application',
              'CLASSES': 'none',
              'EMAIL': 'maciej@opencsw.org',
              'HOTLINE': 'http://www.opencsw.org/bugtrack/',
              'NAME': 'sudo_common - Common files for sudo',
              'OPENCSW_CATALOGNAME': 'sudo_common',
              'OPENCSW_MODE64': '32',
              'OPENCSW_REPOSITORY': 'https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/pkg/sudo/trunk@8935',
              'PKG': 'CSWsudo-common',
              'PSTAMP': 'maciej@build8s-20100302104744',
              'VENDOR': 'ftp://ftp.sudo.ws/pub/sudo/ packaged for CSW by Maciej Blizinski',
              'VERSION': '1.7.2p5,REV=2010.03.02',
              'WORKDIR_FIRSTMOD': '../build-isa-sparcv8'},
  'pkgmap': [{'class': None,
              'group': None,
              'line': ': 1 557',
              'mode': None,
              'path': None,
              'type': '1',
              'user': None},
             {'class': 'none',
              'group': 'bin',
              'line': '1 f none /opt/csw/etc/sudoers.CSW 0644 root bin 715 61323 1267522149',
              'mode': '0644',
              'path': '/opt/csw/etc/sudoers.CSW',
              'type': 'f',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 d none /opt/csw/libexec 0755 root bin',
              'mode': '0755',
              'path': '/opt/csw/libexec',
              'type': 'd',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 f none /opt/csw/libexec/sudo_noexec.so 0755 root bin 5996 42161 1267522148',
              'mode': '0755',
              'path': '/opt/csw/libexec/sudo_noexec.so',
              'type': 'f',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 f none /opt/csw/sbin/visudo 0755 root bin 146604 53853 1267522152',
              'mode': '0755',
              'path': '/opt/csw/sbin/visudo',
              'type': 'f',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 d none /opt/csw/share/doc/sudo_common 0755 root bin',
              'mode': '0755',
              'path': '/opt/csw/share/doc/sudo_common',
              'type': 'd',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 f none /opt/csw/share/doc/sudo_common/license 0644 root bin 4423 15997 1267523256',
              'mode': '0644',
              'path': '/opt/csw/share/doc/sudo_common/license',
              'type': 'f',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 d none /opt/csw/share/man/man1m 0755 root bin',
              'mode': '0755',
              'path': '/opt/csw/share/man/man1m',
              'type': 'd',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 f none /opt/csw/share/man/man1m/sudo.1m 0644 root bin 33335 56127 1267522150',
              'mode': '0644',
              'path': '/opt/csw/share/man/man1m/sudo.1m',
              'type': 'f',
              'user': 'root'},
             {'class': 'none',
              'group': None,
              'line': '1 l none /opt/csw/share/man/man1m/sudoedit.1m=/opt/csw/share/man/man1m/sudo.1m',
              'mode': None,
              'path': '/opt/csw/share/man/man1m/sudoedit.1m',
              'type': 'l',
              'user': None},
             {'class': 'none',
              'group': 'bin',
              'line': '1 f none /opt/csw/share/man/man1m/visudo.1m 0644 root bin 12144 63550 1267522150',
              'mode': '0644',
              'path': '/opt/csw/share/man/man1m/visudo.1m',
              'type': 'f',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 d none /opt/csw/share/man/man4 0755 root bin',
              'mode': '0755',
              'path': '/opt/csw/share/man/man4',
              'type': 'd',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 f none /opt/csw/share/man/man4/sudoers.4 0644 root bin 71819 39000 1267522151',
              'mode': '0644',
              'path': '/opt/csw/share/man/man4/sudoers.4',
              'type': 'f',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 d none /var/opt/csw/log 0755 root bin',
              'mode': '0755',
              'path': '/var/opt/csw/log',
              'type': 'd',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 d none /var/opt/csw/log/sudo 0755 root bin',
              'mode': '0755',
              'path': '/var/opt/csw/log/sudo',
              'type': 'd',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 d none /var/opt/csw/log/sudo/logs 0755 root bin',
              'mode': '0755',
              'path': '/var/opt/csw/log/sudo/logs',
              'type': 'd',
              'user': 'root'},
             {'class': None,
              'group': None,
              'line': '1 i copyright 75 7112 1267523256',
              'mode': None,
              'path': None,
              'type': 'i',
              'user': None},
             {'class': None,
              'group': None,
              'line': '1 i depend 110 9928 1267523264',
              'mode': None,
              'path': None,
              'type': 'i',
              'user': None},
             {'class': None,
              'group': None,
              'line': '1 i pkginfo 491 41276 1267523267',
              'mode': None,
              'path': None,
              'type': 'i',
              'user': None},
             {'class': None,
              'group': None,
              'line': '1 i postinstall 321 26084 1237750445',
              'mode': None,
              'path': None,
              'type': 'i',
              'user': None}]},
 {'bad_paths': {},
  'basic_stats': {'catalogname': 'sudo',
                  'md5_sum': 'dce7f8da0edbb80ec4bdf697ccfc1846',
                  'parsed_basename': {'arch': 'sparc',
                                      'catalogname': 'sudo',
                                      'full_version_string': '1.7.2p5,REV=2010.03.02',
                                      'osrel': 'SunOS5.8',
                                      'revision_info': {'REV': '2010.03.02'},
                                      'vendortag': 'CSW',
                                      'version': '1.7.2p5',
                                      'version_info': {'major version': '1',
                                                       'minor version': '7',
                                                       'patchlevel': '2p5'}},
                  'pkg_basename': 'sudo-1.7.2p5,REV=2010.03.02-SunOS5.8-sparc-CSW.pkg.gz',
                  'pkg_path': '/tmp/pkg_CGJ5ja/sudo-1.7.2p5,REV=2010.03.02-SunOS5.8-sparc-CSW.pkg.gz',
                  'pkgname': 'CSWsudo',
                  'stats_version': 9L},
  'binaries': ['opt/csw/bin/sudo.minimal'],
  'binaries_dump_info': [{'RPATH set': True,
                          'RUNPATH RPATH the same': True,
                          'RUNPATH set': True,
                          'base_name': 'sudo.minimal',
                          'needed sonames': ('libpam.so.1',
                                             'libdl.so.1',
                                             'libintl.so.8',
                                             'libsocket.so.1',
                                             'libnsl.so.1',
                                             'libc.so.1'),
                          'path': 'opt/csw/bin/sudo.minimal',
                          'runpath': ('/opt/csw/lib/$ISALIST',
                                      '/opt/csw/lib')}],
  'depends': [('CSWalternatives',
               'CSWalternatives alternatives - Alternatives engine from Red Hat chkconfig-1.3.30c '),
              ('CSWcommon',
               'CSWcommon common - common files and dirs for CSW packages '),
              ('CSWsudo-common',
               'CSWsudo-common sudo_common - Common files for sudo '),
              ('CSWggettextrt',
               'CSWggettextrt ggettextrt - GNU locale utilities ')],
  'files_metadata': [{'endian': 'Big endian',
                      'machine_id': 2,
                      'mime_type': 'application/x-executable; charset=binary',
                      'mime_type_by_hachoir': u'application/x-executable',
                      'path': 'opt/csw/bin/sudo.minimal'},
                     {'mime_type': 'text/plain; charset=us-ascii',
                      'path': 'opt/csw/share/alternatives/sudo'},
                     {'mime_type': 'text/plain; charset=us-ascii',
                      'path': 'opt/csw/share/doc/sudo/license'}],
  'isalist': ('sparcv9+vis2',
              'sparcv9+vis',
              'sparcv9',
              'sparcv8plus+vis2',
              'sparcv8plus+vis',
              'sparcv8plus',
              'sparcv8',
              'sparcv8-fsmuld',
              'sparcv7',
              'sparc'),
  'ldd_info': {'opt/csw/bin/sudo.minimal': []},
  'binaries_elf_info': {
      'opt/csw/bin/sudo.minimal': {
        'version definition': [],
        'version needed': [],
        'symbol table': [
          { 'soname': 'libpam.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
          { 'soname': 'libdl.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
          { 'soname': 'libintl.so.8', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
          { 'soname': 'libsocket.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
          { 'soname': 'libnsl.so.1', 'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
          { 'soname': 'libc.so.1',  'symbol': 'foo', 'flags': 'DBL', 'shndx': 'UNDEF', 'bind': 'GLOB' },
        ]
      }
  },
  'mtime': datetime.datetime(2010, 3, 2, 22, 34, 39),
  'overrides': [],
  'pkgchk': {'return_code': 0,
             'stderr_lines': ['rm: Cannot remove any directory in the path of the current working directory',
                              '/var/tmp/aaaJFaizt/CSWsudo'],
             'stdout_lines': ['Checking uninstalled stream format package <CSWsudo> from </tmp/pkg_CGJ5ja/sudo-1.7.2p5,REV=2010.03.02-SunOS5.8-sparc-CSW.pkg>',
                              '## Checking control scripts.',
                              '## Checking package objects.',
                              '## Checking is complete.']},
  'pkginfo': {'ARCH': 'sparc',
              'CATEGORY': 'application',
              'CLASSES': 'none cswalternatives',
              'EMAIL': 'maciej@opencsw.org',
              'HOTLINE': 'http://www.opencsw.org/bugtrack/',
              'NAME': 'sudo - Provides limited super user privileges',
              'OPENCSW_CATALOGNAME': 'sudo',
              'OPENCSW_MODE64': '32',
              'OPENCSW_REPOSITORY': 'https://gar.svn.sourceforge.net/svnroot/gar/csw/mgar/pkg/sudo/trunk@8935',
              'PKG': 'CSWsudo',
              'PSTAMP': 'maciej@build8s-20100302104739',
              'VENDOR': 'ftp://ftp.sudo.ws/pub/sudo/ packaged for CSW by Maciej Blizinski',
              'VERSION': '1.7.2p5,REV=2010.03.02',
              'WORKDIR_FIRSTMOD': '../build-isa-sparcv8'},
  'pkgmap': [{'class': None,
              'group': None,
              'line': ': 1 461',
              'mode': None,
              'path': None,
              'type': '1',
              'user': None},
             {'class': 'none',
              'group': 'bin',
              'line': '1 f none /opt/csw/bin/sudo.minimal 4755 root bin 224092 24233 1267522152',
              'mode': '4755',
              'path': '/opt/csw/bin/sudo.minimal',
              'type': 'f',
              'user': 'root'},
             {'class': 'none',
              'group': None,
              'line': '1 l none /opt/csw/bin/sudoedit.minimal=/opt/csw/bin/sudo.minimal',
              'mode': None,
              'path': '/opt/csw/bin/sudoedit.minimal',
              'type': 'l',
              'user': None},
             {'class': 'none',
              'group': 'bin',
              'line': '1 d none /opt/csw/share/alternatives 0755 root bin',
              'mode': '0755',
              'path': '/opt/csw/share/alternatives',
              'type': 'd',
              'user': 'root'},
             {'class': 'cswalternatives',
              'group': 'bin',
              'line': '1 f cswalternatives /opt/csw/share/alternatives/sudo 0644 root bin 125 10881 1267522155',
              'mode': '0644',
              'path': '/opt/csw/share/alternatives/sudo',
              'type': 'f',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 d none /opt/csw/share/doc/sudo 0755 root bin',
              'mode': '0755',
              'path': '/opt/csw/share/doc/sudo',
              'type': 'd',
              'user': 'root'},
             {'class': 'none',
              'group': 'bin',
              'line': '1 f none /opt/csw/share/doc/sudo/license 0644 root bin 4423 15997 1267523256',
              'mode': '0644',
              'path': '/opt/csw/share/doc/sudo/license',
              'type': 'f',
              'user': 'root'},
             {'class': None,
              'group': None,
              'line': '1 i copyright 68 6368 1267523256',
              'mode': None,
              'path': None,
              'type': 'i',
              'user': None},
             {'class': None,
              'group': None,
              'line': '1 i depend 247 22297 1267523258',
              'mode': None,
              'path': None,
              'type': 'i',
              'user': None},
             {'class': None,
              'group': None,
              'line': '1 i pkginfo 503 42551 1267523262',
              'mode': None,
              'path': None,
              'type': 'i',
              'user': None}]}]
