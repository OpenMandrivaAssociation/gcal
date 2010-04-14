Summary:	Print calendars
Name:		gcal
Version:	3.5.1
Release:	%mkrel 1
License:	GPLv3+
Group:		Office
Source0:	ftp://ftp.gnu.org/pub/gnu/gcal/%{name}-%{version}.tar.bz2
#Patch0:		gcal-fix-relative-symlinks.patch
URL:		http://www.gnu.org/software/gcal/gcal.html
BuildRequires:	ncurses-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
Gcal is a program for printing calendars. Gcal displays a calendar for a month
or a year, eternal holiday lists and fixed date lists, in many ways. The
program correctly omits the dates that were skipped when the current Gregorian
calendar replaced the earlier Julian calendar.

Additionally, it can generate air line distance between over 400 cities on
earth, moon phases in these cities, whole annual holidays, etc.

%prep
%setup -q
#%patch0 -p0

%build
%configure --with-included-regexps
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} mandir=$RPM_BUILD_ROOT%{_mandir}/man1
perl -pi -e "s,$RPM_BUILD_ROOT,," $RPM_BUILD_ROOT/usr/share/gcal/misc/*/*

mkdir -p $RPM_BUILD_ROOT%{_mandir}/de/man1
rm -f $RPM_BUILD_ROOT%{_datadir}/locale/*.alias
rm -f $RPM_BUILD_ROOT%{_infodir}/dir.texi*

%find_lang %{name}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc README COPYING AUTHORS NEWS THANKS 
%{_bindir}/*
%{_datadir}/gcal
%{_infodir}/gcal*

