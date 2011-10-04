# Define this to link to which library version  eg. /lib64/ld-lsb-x86-64.so.3
%define lsbsover 3 

%ifarch %{ix86}
%define ldso ld-linux.so.2
%define lsbldso ld-lsb.so
%endif


%ifarch x86_64
%define ldso ld-linux-x86-64.so.2
%define lsbldso ld-lsb-x86-64.so
%endif

%define qual %{nil}

%define upstreamlsbrelver 2.0
%define lsbrelver 4.0
%define srcrelease 1

Summary: LSB support for Moblin Linux
Name: meego-lsb
Version: 4.0
Release: 1
URL: http://www.linux-foundation.org/
Source0: %{name}-%{version}-%{srcrelease}.tar.bz2
Source1: lsb-release-%{upstreamlsbrelver}.tar.gz
Patch0: lsb-release.patch
Patch1: fix-building-error.patch
License: GPLv2
Group: System/Base
BuildRoot: %{_tmppath}/%{name}-root
BuildRequires: glibc-static
# dependency for primary LSB application for v1.3
Provides: lsb = %{version}
# dependency for primary LSB application for v2.0 and v3.0
%ifarch %{ix86}
%define archname ia32
%endif
%ifarch x86_64
%define archname amd64
%endif
%ifarch %{arm}
%define archname arm
%endif
Provides: lsb-core-%{archname} = %{version}
Provides: lsb-graphics-%{archname} = %{version}
Provides: lsb-core-noarch = %{version}
Provides: lsb-graphics-noarch = %{version}


%ifarch %{ix86}
# archLSB IA32 Base Libraries
Requires: libc.so.6
Requires: libm.so.6
%endif


# gLSB Base/Utility/Stdc++/Graphics Libraries
Requires: libasound.so.2%{qual}
Requires: libatk-1.0.so.0%{qual}
Requires: libcairo.so.2%{qual}
Requires: libcrypt.so.1%{qual}
Requires: libcups.so.2%{qual}
Requires: libcupsimage.so.2%{qual}
Requires: libdl.so.2%{qual}
Requires: libfontconfig.so.1%{qual}
Requires: libfreetype.so.6%{qual}
Requires: libgcc_s.so.1%{qual}
Requires: libgdk-x11-2.0.so.0%{qual}
Requires: libgdk_pixbuf-2.0.so.0%{qual}
Requires: libgdk_pixbuf_xlib-2.0.so.0%{qual}
Requires: libGL.so.1%{qual}
Requires: libglib-2.0.so.0%{qual}
Requires: libGLU.so.1%{qual}
Requires: libgmodule-2.0.so.0%{qual}
Requires: libgobject-2.0.so.0%{qual}
Requires: libgthread-2.0.so.0%{qual}
Requires: libgtk-x11-2.0.so.0%{qual}
Requires: libICE.so.6%{qual}
Requires: libjpeg.so.62%{qual}
Requires: libncurses.so.5%{qual}
Requires: libnspr4.so%{qual}
Requires: libnss3.so%{qual}
Requires: libpam.so.0%{qual}
Requires: libpango-1.0.so.0%{qual}
Requires: libpangocairo-1.0.so.0%{qual}
Requires: libpangoft2-1.0.so.0%{qual}
Requires: libpangoxft-1.0.so.0%{qual}
Requires: libpng12.so.0%{qual}
Requires: libpthread.so.0%{qual}
Requires: libQtCore.so.4%{qual}
Requires: libQtGui.so.4%{qual}
Requires: libQtNetwork.so.4%{qual}
Requires: libQtOpenGL.so.4%{qual}
Requires: libQtSql.so.4%{qual}
Requires: libQtSvg.so.4%{qual}
Requires: libQtXml.so.4%{qual}
Requires: librt.so.1%{qual}
Requires: libSM.so.6%{qual}
Requires: libssl3.so%{qual}
Requires: libstdc++.so.6%{qual}
Requires: libutil.so.1%{qual}
Requires: libX11.so.6%{qual}
Requires: libXext.so.6%{qual}
Requires: libXft.so.2%{qual}
Requires: libXi.so.6%{qual}
Requires: libxml2.so.2%{qual}
Requires: libXrender.so.1%{qual}
Requires: libXt.so.6%{qual}
Requires: libXtst.so.6%{qual}
Requires: libz.so.1%{qual}

# gLSB Command and Utilities
Requires: /bin/awk
Requires: /bin/basename
Requires: /bin/cat
Requires: /bin/chgrp
Requires: /bin/chmod
Requires: /bin/chown
Requires: /bin/cp
Requires: /usr/bin/cpio
Requires: /bin/cut
Requires: /bin/date
Requires: /bin/dd
Requires: /bin/df
Requires: /bin/dmesg
Requires: /bin/echo
Requires: /bin/ed
Requires: /bin/egrep
Requires: /bin/env
Requires: /bin/false
Requires: /bin/fgrep
Requires: /bin/find
Requires: /usr/bin/gettext
Requires: /bin/grep
Requires: /bin/gunzip
Requires: /bin/gzip
Requires: /bin/hostname
Requires: /bin/kill
Requires: /bin/ln
Requires: /bin/ls
Requires: mailx
Requires: /bin/mkdir
Requires: /bin/mknod
Requires: /bin/mktemp
Requires: /bin/more
Requires: /bin/mount
Requires: /bin/mv
Requires: /bin/nice
Requires: /bin/ps
Requires: /bin/pwd
Requires: /bin/rm
Requires: /bin/rmdir
Requires: /bin/sed
Requires: /bin/sh
Requires: /bin/sleep
Requires: /bin/sort
Requires: /bin/stty
Requires: /bin/su
Requires: /bin/sync
Requires: /bin/tar
Requires: /bin/touch
Requires: /bin/true
Requires: /bin/umount
Requires: /bin/uname
Requires: /bin/zcat
Requires: /sbin/fuser
Requires: /sbin/pidof
Requires: /sbin/shutdown
Requires: /usr/bin/[
Requires: /usr/bin/ar
Requires: /usr/bin/at
Requires: /usr/bin/batch
Requires: /usr/bin/bc
Requires: /usr/bin/chfn
Requires: /usr/bin/chsh
Requires: /usr/bin/cksum
Requires: /usr/bin/cmp
Requires: /usr/bin/col
Requires: /usr/bin/comm
Requires: /usr/bin/crontab
Requires: /usr/bin/csplit
Requires: /usr/bin/diff
Requires: /usr/bin/dirname
Requires: /usr/bin/du
Requires: /usr/bin/expand
Requires: /usr/bin/expr
Requires: /usr/bin/fc-cache
Requires: /usr/bin/fc-list
Requires: /usr/bin/fc-match
Requires: /usr/bin/file
Requires: /usr/bin/fold
Requires: /usr/bin/foomatic-rip
Requires: /usr/bin/gencat
Requires: /usr/bin/getconf
Requires: /usr/bin/groups
Requires: /usr/bin/gs
Requires: /usr/bin/head
Requires: /usr/bin/iconv
Requires: /usr/bin/id
Requires: /usr/bin/install
Requires: /usr/bin/ipcrm
Requires: /usr/bin/ipcs
Requires: /usr/bin/join
Requires: /usr/bin/killall
Requires: /usr/bin/locale
Requires: /usr/bin/localedef
Requires: /usr/bin/logger
Requires: /usr/bin/logname
Requires: /usr/bin/lp
Requires: /usr/bin/lpr
Requires: /usr/bin/m4
Requires: /usr/bin/make
Requires: /usr/bin/man
Requires: /usr/bin/md5sum
Requires: /usr/bin/mkfifo
Requires: /usr/bin/msgfmt
Requires: /usr/bin/newgrp
Requires: /usr/bin/nl
Requires: /usr/bin/nohup
Requires: /usr/bin/od
Requires: /usr/bin/passwd
Requires: /usr/bin/paste
Requires: /usr/bin/patch
Requires: /usr/bin/pathchk
Requires: /usr/bin/pax
Requires: /usr/bin/perl
Requires: /usr/bin/pr
Requires: /usr/bin/printf
Requires: /usr/bin/python
Requires: /usr/bin/renice
Requires: /usr/bin/seq
Requires: /usr/bin/split
Requires: /usr/bin/strip
Requires: /usr/bin/tail
Requires: /usr/bin/tee
Requires: /usr/bin/test
Requires: /usr/bin/time
Requires: /usr/bin/tr
Requires: /usr/bin/tsort
Requires: /usr/bin/tty
Requires: /usr/bin/unexpand
Requires: /usr/bin/uniq
Requires: /usr/bin/wc
Requires: /usr/bin/xargs
Requires: /usr/bin/xdg-desktop-icon
Requires: /usr/bin/xdg-desktop-menu
Requires: /usr/bin/xdg-email
Requires: /usr/bin/xdg-icon-resource
Requires: /usr/bin/xdg-mime
Requires: /usr/bin/xdg-open
Requires: /usr/bin/xdg-screensaver
Requires: /usr/sbin/groupadd
Requires: /usr/sbin/groupdel
Requires: /usr/sbin/groupmod
Requires: /usr/lib/sendmail
Requires: /usr/sbin/useradd
Requires: /usr/sbin/userdel
Requires: /usr/sbin/usermod

Requires: lsb-release

%description
The Linux Standard Base (LSB) is an attempt to develop a set of
standards that will increase compatibility among Linux distributions.
The meego-lsb package provides utilities needed for LSB Compliant
Applications.  It also contains requirements that will ensure that all
components required by the LSB that are provided by Red Hat Linux are
installed on the system.


%package -n lsb-release
Summary: LSB Release Script
Group: System/Base


%description -n lsb-release
LSB Release Script

%prep
%setup -q -a 1
%patch0 -p1
%patch1 -p1

%build
cd lsb-release-%{upstreamlsbrelver}
make

%pre
# remove the extra symlink /bin/mailx -> /bin/mail
  if [ -e /bin/mailx ]; then
    if [ -L /bin/mailx ]; then
      rm -f /bin/mailx
    fi
  fi

%install
rm -rf %{buildroot}
# LSB uses /usr/lib rather than /usr/lib64 even for 64bit OS
mkdir -p %{buildroot}%{_sysconfdir} %{buildroot}/%{_lib} %{buildroot}%{_mandir} \
         %{buildroot}%{_bindir} %{buildroot}/usr/lib/lsb \
         %{buildroot}%{_sysconfdir}/lsb-release.d/ %{buildroot}%{_sbindir}
make DESTDIR=%{buildroot} install
cd lsb-release-%{upstreamlsbrelver}
make mandir=%{buildroot}/%{_mandir} prefix=%{buildroot}/%{_prefix} install
cd ..
touch %{buildroot}/etc/lsb-release.d/core-4.0-%{archname}
touch %{buildroot}/etc/lsb-release.d/core-4.0-noarch
touch %{buildroot}/etc/lsb-release.d/desktop-4.0-%{archname}
touch %{buildroot}/etc/lsb-release.d/desktop-4.0-noarch
# and claim LSB 3.1, 3.2 are supported as well
touch %{buildroot}/etc/lsb-release.d/core-3.2-%{archname}
touch %{buildroot}/etc/lsb-release.d/core-3.2-noarch
touch %{buildroot}/etc/lsb-release.d/desktop-3.2-%{archname}
touch %{buildroot}/etc/lsb-release.d/desktop-3.2-noarch
touch %{buildroot}/etc/lsb-release.d/core-3.1-%{archname}
touch %{buildroot}/etc/lsb-release.d/core-3.1-noarch
touch %{buildroot}/etc/lsb-release.d/desktop-3.1-%{archname}
touch %{buildroot}/etc/lsb-release.d/desktop-3.1-noarch

for LSBVER in %{lsbsover}; do
  ln -s %{ldso} %{buildroot}/%{_lib}/%{lsbldso}.$LSBVER
done

mkdir -p %{buildroot}/bin

# LSB uses /usr/lib rather than /usr/lib64 even for 64bit OS
# According to the lsb-core documentation provided by 
# http://refspecs.linux-foundation.org/LSB_4.0.0/LSB-Core-generic/LSB-Core-generic.pdf
# it's OK to put non binary in /usr/lib.
#ln -snf ../../../sbin/chkconfig %{buildroot}/usr/lib/lsb/install_initd
#ln -snf ../../../sbin/chkconfig %{buildroot}/usr/lib/lsb/remove_initd
# ln -snf mail %{buildroot}/bin/mailx

#mkdir -p %{buildroot}/usr/X11R6/lib/X11/xserver
#ln -snf /usr/%{_lib}/xserver/SecurityPolicy %{buildroot}/usr/X11R6/lib/X11/xserver/SecurityPolicy
#ln -snf /usr/share/X11/fonts %{buildroot}/usr/X11R6/lib/X11/fonts
#ln -snf /usr/share/X11/rgb.txt  %{buildroot}/usr/X11R6/lib/X11/rgb.txt

# According to https://bugzilla.redhat.com/show_bug.cgi?id=232918 , the '-static' option
# is imported against segfault error while running redhat_lsb_trigger
#gcc $RPM_OPT_FLAGS -Os -static -o meego_lsb_trigger{.%{_target_cpu},.c} -DLSBSOVER='"%{lsbsover}"' \
#  -DLDSO='"%{ldso}"' -DLSBLDSO='"/%{_lib}/%{lsbldso}"' -D_GNU_SOURCE
#install -m 700 meego_lsb_trigger.%{_target_cpu} \
#  %{buildroot}%{_sbindir}/meego_lsb_trigger.%{_target_cpu}

cp -p meego_lsb_init %{buildroot}/bin/meego_lsb_init

%clean
rm -rf %{buildroot}

#%triggerpostun -- glibc
#if [ -x /usr/sbin/meego_lsb_trigger.%{_target_cpu} ]; then
#  /usr/sbin/meego_lsb_trigger.%{_target_cpu}
#fi

%ifnarch %{ix86}
  /sbin/sln %{ldso} /%{_lib}/%{lsbldso} || :
%else
  if [ -f /emul/ia32-linux/lib/%{ldso} ]; then
    for LSBVER in %{lsbsover}; do
      /sbin/sln /emul/ia32-linux/lib/%{ldso} /%{_lib}/%{lsbldso}.$LSBVER || :
    done
  else
    for LSBVER in %{lsbsover}; do
      /sbin/sln %{ldso} /%{_lib}/%{lsbldso}.$LSBVER || :
    done
  fi
%endif

%ifarch %{ix86}
%post
# make this softlink again for /emul
  if [ -f /emul/ia32-linux/lib/%{ldso} ]; then
    for LSBVER in %{lsbsover}; do
      /sbin/sln /emul/ia32-linux/lib/%{ldso} /%{_lib}/%{lsbldso}.$LSBVER || :
    done
  fi
%endif

%files
%{_sysconfdir}/meego-lsb
%dir %{_sysconfdir}/lsb-release.d
%{_mandir}/*/*
%{_bindir}/*
%exclude %{_bindir}/lsb_release
/bin/meego_lsb_init
/usr/lib/lsb
/%{_lib}/*so*
/lib/lsb*

%files -n lsb-release
%defattr(-,root,root,-)
%dir %{_sysconfdir}/lsb-release.d
%{_sysconfdir}/lsb-release.d/*
%{_bindir}/lsb_release
