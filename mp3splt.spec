Summary:   A Free, command-line, AlbumWrap and mp3wrap file exctractor
Name:      mp3splt
Version:   2.6.2
Release:   6%{?dist}
License:   GPLv2
Group:     Applications/Multimedia
Source:    http://download.sourceforge.net/sourceforge/mp3splt/mp3splt-%{version}.tar.gz
URL:       http://mp3splt.sourceforge.net/
BuildRequires: libmp3splt-devel > 0.7.0
BuildRequires: libtool-ltdl-devel
BuildRequires: gettext

%description
Mp3Splt is a command line utility to split mp3 and ogg files,
by selecting a begin and an end time position, without decoding.
It is very useful to split large mp3/ogg into smaller files,
or to split entire albums to obtain original tracks.
To split an album, the split points and filenames can be selected
manually or automatically from CDDB (internet or a local file),
or from .cue files.

It supports VBR mp3, and it is also possible to extract tracks
from Mp3Wrap or AlbumWrap files in a few seconds.

%prep
%setup -q
%{_bindir}/iconv -f iso8859-1 -t utf8 AUTHORS -o AUTHORS.txt
touch -r AUTHORS AUTHORS.txt
mv AUTHORS.txt AUTHORS

%build
%configure --enable-oggsplt_symlink --disable-static

%__make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%find_lang %{name}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr (-,root,root,-)
%doc AUTHORS README
%license COPYING
%{_bindir}/mp3splt
%{_bindir}/oggsplt
%{_mandir}/man1/%{name}*.gz
%{_mandir}/man1/oggsplt.1.gz

%changelog
* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 27 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Mon Mar 20 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 02 2015 Sérgio Basto <sergio@serjux.com> - 2.6.2-1
- Update to 2.6.2.

* Fri Aug 30 2013 Paulo Roma <roma@lcg.ufrj.br> 2.6-13
- Updated to 2.6

* Sun Mar 31 2013 Paulo Roma <roma@lcg.ufrj.br> 2.5.2-12
- Updated to 2.5.2

* Fri Sep 07 2012 Paulo Roma <roma@lcg.ufrj.br> 2.4.3-11
- Updated to 2.4.3

* Wed Jun 06 2012 Paulo Roma <roma@lcg.ufrj.br> 2.4.2-10
- Updated to 2.4.2

* Wed Jan 04 2012 Paulo Roma <roma@lcg.ufrj.br> 2.4.1-9
- Updated to 2.4.1

* Sat Sep 03 2011 Paulo Roma <roma@lcg.ufrj.br> 2.4-8
- Updated to 2.4

* Sun Mar 13 2011 Paulo Roma <roma@lcg.ufrj.br> 2.3a-7
- Updated to 2.3a

* Mon Sep 27 2010 Paulo Roma <roma@lcg.ufrj.br> 2.2.9-6
- Updated to 2.2.9

* Wed Feb 17 2010 Paulo Roma <roma@lcg.ufrj.br> 2.2.8-6
- Updated to 2.2.8

* Wed Nov 04 2009 Paulo Roma <roma@lcg.ufrj.br> 2.2.7a-6
- Updated to 2.2.7a

* Sat Oct 31 2009 Paulo Roma <roma@lcg.ufrj.br> 2.2.7-6
- Updated to 2.2.7

* Thu Jul 30 2009 Paulo Roma <roma@lcg.ufrj.br> 2.2.6a-6
- Bugfix release: 2.2.6a

* Mon Jul 27 2009 Paulo Roma <roma@lcg.ufrj.br> 2.2.6-6
- Updated to 2.2.6
- Using find_lang.

* Sat May 16 2009 Paulo Roma <roma@lcg.ufrj.br> 2.2.5-5
- Updated to 2.2.5

* Mon May 11 2009 Paulo Roma <roma@lcg.ufrj.br> 2.2.4-5
- Added BR libtool-ltdl-devel.

* Sat May 09 2009 Paulo Roma <roma@lcg.ufrj.br> 2.2.4-4
- Updated to 2.2.4
- Touching AUTHORS file.
- Updated Source download link.
- Removed obsolete gcc 4.1 patch.

* Wed Jul 30 2008 Paulo Roma <roma@lcg.ufrj.br> 2.1-3
- Patched for building on gcc 4.1.
- Converted AUTHORS to utf8.

* Sat Nov 17 2007 Paulo Roma <roma@lcg.ufrj.br> 2.1-2
- Using CC=gcc and relying on forcegcc
  for chosing the appropriate compiler (gcc34 or gcc32).

* Thu Jul 12 2007 Paulo Roma <roma@lcg.ufrj.br> 2.1-1
- Initial spec file.
