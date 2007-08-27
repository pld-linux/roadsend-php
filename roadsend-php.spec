# TODO
# - package files
Summary:	The Roadsend PCC Compiler for PHP
Summary(pl.UTF-8):	Kompilator Roadsend PCC dla PHP
Name:		roadsend-php
Version:	2.9.2
Release:	0.1
License:	GPL / LGPL
Group:		Development/Languages
Source0:	http://code.roadsend.com/snaps/%{name}-%{version}.tar.bz2
# Source0-md5:	c7492681aa6f5f0fd7b7fd5d44e6996d
Patch0:		%{name}-ac.patch
URL:		http://www.roadsend.com/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	bigloo >= 2.9a
BuildRequires:	curl-devel >= 7.15.0
BuildRequires:	fcgi-devel >= 2.4.0
BuildRequires:	gtk+2-devel
BuildRequires:	libglade2-devel
BuildRequires:	libidn-devel
BuildRequires:	libssh2-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 1:2.6.0
BuildRequires:	mysql-devel
BuildRequires:	pcre-devel >= 6.3
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
pomoc± PHP mo¿e, ale nie musi byæOF u¿yty razem z serwerem HTTP
Apache.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%configure \
	--with-gtk2
%{__make} -j1

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
