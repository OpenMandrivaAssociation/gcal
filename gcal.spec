%define	name	gcal
%define	version	3.01.1
%define	release	%mkrel 1

Summary:	Print calendars
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Office
Source0:	ftp://ftp.gnu.org/pub/gnu/gcal/%{name}-%{version}.tar.bz2
Patch0:		gcal-fix-relative-symlinks.patch.bz2
Patch1:		%{name}-3.01-misc.patch.bz2
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
%patch0 -p0
%patch1 -p1

%build
%configure --with-included-regexps
%make

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} mandir=$RPM_BUILD_ROOT%{_mandir}/man1
perl -pi -e "s,$RPM_BUILD_ROOT,," $RPM_BUILD_ROOT/usr/share/gcal/misc/*/*

mkdir -p $RPM_BUILD_ROOT%{_mandir}/de/man1
install -m0644 doc/de/man/*.1 $RPM_BUILD_ROOT%{_mandir}/de/man1/

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
%doc README LIMITATIONS COPYING ATTENTION HISTORY DISCLAIM
%{_bindir}/*
%{_datadir}/gcal
%{_infodir}/gcal*
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*

