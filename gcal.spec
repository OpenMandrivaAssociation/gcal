Summary:	Program for calculating and printing calendars
Name:		gcal
Version:	3.6
Release:	3
License:	GPLv3+
Group:		Office
Source0:	ftp://ftp.gnu.org/pub/gnu/gcal/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/gcal/
BuildRequires:	ncurses-devel
BuildRequires:	texinfo
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Gcal is a program for calculating and printing calendars. Gcal displays
hybrid and proleptic Julian and Gregorian calendar sheets, respectively
for one month, three months, or a whole year. It also displays eternal
holiday lists for many countries around the globe, and features a very
powerful creation of fixed date lists that can be used for reminding
purposes.

Gcal can calculate various astronomical data and times of the Sun and
the Moon for pleasure at any location, precisely enough for most civil
purposes. Gcal supports some other calendar systems, for example, the
Chinese and Japanese calendars, the Hebrew calendar, and the civil
Islamic calendar, too.

%prep
%setup -q

sed -i -e "s,ThisGcal=.*,ThisGcal=@PACKAGE@,g" misc/*/*.in

%build
%configure2_5x --disable-rpath MAKEINFO="makeinfo"
%make
%make html

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

#examples
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -rf doc/en/examples %{buildroot}%{_docdir}/%{name}/

#misc files
cp -rf misc %{buildroot}%{_docdir}/%{name}/

#fix rights
chmod 644 %{buildroot}%{_docdir}/%{name}/misc/gcalltx/gcalltx.pl
chmod 755 %{buildroot}%{_docdir}/%{name}/misc/wloc/wlocdrv

for i in daily ddiff dst gcalltx moon mrms srss
do
  chmod 755 %{buildroot}%{_docdir}/%{name}/misc/$i/$i
done

#cleanup
rm -rf %{buildroot}%{_datadir}/%{name}/{CREDITS,README}
find %{buildroot} -name "Makefile*" -exec rm -rf {} \;
find %{buildroot}%{_docdir} -name "*.in" -exec rm -rf {} \;
find %{buildroot}%{_docdir} -name "*.bat" -exec rm -rf {} \;
find %{buildroot}%{_docdir} -name "*.texi" -exec rm -rf {} \;



%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc doc/en/gcal.html doc/GREG-REFORM README BUGS LIMITATIONS TODO AUTHORS NEWS THANKS 
%{_bindir}/*
%{_datadir}/gcal
%{_infodir}/gcal*


%changelog
* Mon Jul 26 2010 Jani Välimaa <wally@mandriva.org> 3.6-2mdv2011.0
+ Revision: 560886
- fix gcal path in misc scripts
- fix misc scripts rights

* Mon Jul 26 2010 Jani Välimaa <wally@mandriva.org> 3.6-1mdv2011.0
+ Revision: 560778
- install examples and misc files
- change description and summary
- add BR to build gcal.html
- new version 3.6
- sync sources
- clean .spec

* Wed Apr 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.5.1-1mdv2010.1
+ Revision: 534761
- Don't define name, version, release on top of spec
- new version 3.5.1
- drop p1, applied upstream and p0 (but keep p0)
- fix %%install && %%files
- lang(de) is now with the other langs (%%find_lang)
- fix license

* Thu Mar 11 2010 Sandro Cazzaniga <kharec@mandriva.org> 3.01.1-1mdv2010.1
+ Revision: 517924
- Fix License according to the COPYING file.
- Update to 3.01.1

* Thu Feb 11 2010 Funda Wang <fwang@mandriva.org> 3.01-13mdv2010.1
+ Revision: 504125
- fix build

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 3.01-10mdv2008.1
+ Revision: 125489
- kill re-definition of %%buildroot on Pixel's request
- import gcal


* Thu Oct 06 2005 Lenny Cartier <lenny@mandriva.com> 3.01-10mdk
- rebuild

* Thu Jul 29 2004 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 3.01-9mdk
- fix buildrequires
- cleanups

* Thu May 27 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 3.01-8mdk
- rebuild
- clean up a leftover file

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 3.01-7mdk
- rebuild

* Wed Jan 22 2003 Lenny Cartier <lenny@mandrakesoft.com> 3.01-6mdk
- rebuild

* Sun Mar 17 2002 Lenny Cartier <lenny@mandrakesoft.com> 3.01-5mdk
- fixes from Abel Cheung <maddog@linux.org.hk> :
	- Patch1: Misc fixes taken from debian
	- Add missing manpages
	- find_lang
	- Use _install_info and _remove_install_info

* Tue Jul 10 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.01-4mdk
- rebuild

* Fri May 11 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 3.01-3mdk
- use find_lang

* Fri Jan  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 3.01-2mdk
- rebuild

* Tue Aug 31 2000 Lenny Cartier <lenny@mandrakesoft.com> 3.01-1mdk
- macros
- BM

* Sat Jun 10 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.00-2mdk
- better group

* Fri Jun  9 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 3.00-1mdk
- first Mandrake package

