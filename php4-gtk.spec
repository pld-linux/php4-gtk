%define		_modname	gtk
%define		_sysconfdir	/etc/php4
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	PHP language bindings for GTK+ toolkit
Summary(pl.UTF-8):   Moduł PHP z wiązaniami do GTK+
Name:		php4-gtk
Version:	1.0.2
Release:	7
License:	GPL
Group:		Libraries
Source0:	http://gtk.php.net/distributions/php-gtk-%{version}.tar.gz
# Source0-md5:	b11859c0778e40e53a14919a589db464
Patch0:		%{name}-object.patch
Patch1:		%{name}-generator.patch
Patch2:		%{name}-php_path.patch
URL:		http://gtk.php.net/
BuildRequires:	gtk+-devel >= 1:1.2.6
BuildRequires:	libglade-devel
BuildRequires:	php4-cli
BuildRequires:	php4-devel >= 3:4.3.0
BuildRequires:	php4-pcre
BuildRequires:	rpmbuild(macros) >= 1.322
%{?requires_php_extension}
Requires:	php4-cli
Provides:	php(gtk)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PHP-GTK is a PHP extension that enables you to write client-side
cross-platform GUI applications. This is the first such extension of
this kind and one of the goals behind it was to prove that PHP is a
capable general-purpose scripting language that is suited for more
than just Web applications.

This extension will _not_ allow you to display GTK+ programs in a Web
browser, and cannot be used in the Web environment. It is intended for
creating standalone GUI applications.

%description -l pl.UTF-8
PHP-GTK jest rozszerzeniem PHP które pozwala pisać klienckie przenośne
aplikacje typu GUI. To jest pierwsze rozszerzenie tego typu i jednym z
celów które przyświecały jego autorom było pokazanie że PHP jest
językiem skryptowym ogólnego zastosowania, który pasuje do czegoś
więcej niż tylko aplikacje WWW.

To rozszerzenie _nie_pozwala_ na używanie programów korzystających z
GTK+ przez przeglądarkę i nie może być używane w środowisku WWW. Jest
przeznaczone do tworzenia samodzielnych aplikacji GUI.

%prep
%setup -q -n php_gtk-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
phpize
%configure \
	--with-php-config=%{_bindir}/php-config
%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{extensionsdir}
install modules/php_gtk.so $RPM_BUILD_ROOT%{extensionsdir}/%{_modname}.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog AUTHORS TODO NEWS
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
