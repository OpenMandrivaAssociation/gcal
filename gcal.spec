Summary:	Print calendars
Name:		gcal
Version:	3.6
Release:	%mkrel 1
License:	GPLv3+
Group:		Office
Source0:	ftp://ftp.gnu.org/pub/gnu/gcal/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/gcal/
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

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%find_lang %{name}

#cleanup
rm -rf %{buildroot}%{_datadir}/%{name}/{CREDITS,README,Makefile.in}

%post
%_install_info %{name}.info

%preun
%_remove_install_info %{name}.info

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,0755)
%doc README BUGS LIMITATIONS TODO AUTHORS NEWS THANKS 
%{_bindir}/*
%{_datadir}/gcal
%{_infodir}/gcal*
