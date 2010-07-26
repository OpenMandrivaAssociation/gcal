Summary:	Program for calculating and printing calendars
Name:		gcal
Version:	3.6
Release:	%mkrel 1
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
chmod 755 %{buildroot}%{_docdir}/%{name}/misc/gcalltx/gcalltx.pl

#cleanup
rm -rf %{buildroot}%{_datadir}/%{name}/{CREDITS,README}
find %{buildroot} -name "Makefile*" -exec rm -rf {} \;
find %{buildroot}%{_docdir} -name "*.in" -exec rm -rf {} \;
find %{buildroot}%{_docdir} -name "*.bat" -exec rm -rf {} \;
find %{buildroot}%{_docdir} -name "*.texi" -exec rm -rf {} \;

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc doc/en/gcal.html doc/GREG-REFORM README BUGS LIMITATIONS TODO AUTHORS NEWS THANKS 
%{_bindir}/*
%{_datadir}/gcal
%{_infodir}/gcal*
