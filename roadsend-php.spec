# TODO
# - package files
# - fcgi backend
# - gtk2
#
# Conditional build:
%bcond_with	fcgi		# try to build fcgi web backend (fails)
%bcond_with	gtk2		# try to build gtk2 extension (fails)
#
%define		_snap 20070916
Summary:	The Roadsend PCC Compiler for PHP
Summary(pl.UTF-8):	Kompilator Roadsend PCC dla PHP
Name:		roadsend-php
Version:	2.9.2
Release:	0.0.%{_snap}
License:	GPL / LGPL
Group:		Development/Languages
Source0:	http://code.roadsend.com/snaps/%{name}-%{_snap}.tar.bz2
# Source0-md5:	5a89afec3b7dc2826a4960117899f3fc
Patch0:		%{name}-ac.patch
URL:		http://www.roadsend.com/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	bigloo >= 3.0b
BuildRequires:	curl-devel >= 7.15.1
%{?with_fcgi:BuildRequires:	fcgi-devel >= 2.4.0}
%if %{with gtk2}
BuildRequires:	gtk+2-devel >= 1:2.0
BuildRequires:	libglade2-devel >= 1:2.0
%endif
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	mysql-devel
BuildRequires:	pcre-devel >= 6.3
BuildRequires:	pkgconfig
BuildRequires:	sqlite3-devel >= 3.3.0
BuildRequires:	unixODBC-devel >= 2.2.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PCC is the Roadsend PHP Compiler. It compiles PHP code into high
performance stand-alone binaries and libraries. PHP code compiled by
PCC can be used with or without the Apache webserver.

%description -l pl.UTF-8
PCC to kompilator Roadsend dla PHP. Kompiluje on kod PHP w wydajne,
samodzielne pliki wykonywalne oraz biblioteki. Kod skompilowany za
pomocą PHP może, ale nie musi być użyty razem z serwerem HTTP
Apache.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--with%{!?with_gtk:out}-gtk2 \
	--with%{!?with_fcgi:out}-fcgi
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/pcc.conf
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.heap
%{_libdir}/*.sch
%{_libdir}/*.init
%{_libdir}/*.h
