Summary:	PHP language bindings for GTK+ toolkit
Summary(pl):	Modu� PHP z wi�zaniami do GTK+
Name:		php-gtk
Version:	0.0.4
Release:	1
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Source0:	%{name}-%{version}.tar.gz
URL:		http://gtk.php.net/
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	php-devel
BuildRequires:	php-cgi
BuildRequires:	php-pcre
BuildRequires:	libglade-devel
BuildRequires:	gtk+-devel
Requires:	php-cgi
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/php

%description
PHP-GTK is a PHP extension that enables you to write client-side cross-platform
GUI applications. This is the first such extension of this kind and one of the
goals behind it was to prove that PHP is a capable general-purpose scripting
language that is suited for more than just Web applications.

This extension will _not_ allow you to display GTK+ programs in a Web browser,
and cannot be used in the Web environment. It is intended for creating
standalone GUI applications.

%description -l pl
PHP-GTK jest rozszerzeniem PHP kt�re pozwala pisa� klienckie przeno�ne
aplikacje typu GUI. To jest pierwsze roszerzenie tego typu i jednym z
cel�w kt�re przy�wieca�y jego autorom by�o pokazanie �e PHP jest j�zykiem
skryptowym og�lnego zastosowania, kt�ry pasuje do czego� wi�cej ni� tylko
aplikacje webowe.

To roszerzenie _nie_pozwoli_ Ci u�ywa� program�w korzystaj�cych GTK+ przez
przegl�dark� i nie mo�e by� u�ywane w �rodowisku webowym. Jest
przeznaczone do tworzenia samodzielnych aplikacji GUI.

%prep
%setup -q

%build
phpize
aclocal
%configure 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/php

install modules/php_gtk.so $RPM_BUILD_ROOT%{_libdir}/php/gtk.so

gzip -9nf ChangeLog AUTHORS TODO NEWS

%post
%{_sbindir}/php-module-install install gtk %{_sysconfdir}/php.ini

%preun
if [ "$1" = "0" ]; then
        %{_sbindir}/php-module-install remove gtk %{_sysconfdir}/php.ini
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_libdir}/php/*.so
