Summary:	Program for calculating and printing calendars

Name:		gcal
Version:	3.6.3
Release:	1
License:	GPLv3+
Group:		Office
Source0:	ftp://ftp.gnu.org/pub/gnu/gcal/%{name}-%{version}.tar.xz
Patch1:		gcal-3.6.3-texinfo.patch
URL:		http://www.gnu.org/software/gcal/
BuildRequires:	ncurses-devel
BuildRequires:	texinfo

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
%patch1 -p1

sed -i -e "s,ThisGcal=.*,ThisGcal=@PACKAGE@,g" misc/*/*.in

%build
%configure2_5x --disable-rpath MAKEINFO="makeinfo"
%make
%make html

%install
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

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc doc/en/gcal.html doc/GREG-REFORM README BUGS LIMITATIONS TODO AUTHORS NEWS THANKS 
%{_bindir}/*
%{_datadir}/gcal
%{_infodir}/gcal*


