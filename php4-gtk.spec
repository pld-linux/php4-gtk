%define		_modname	gtk
%define		_sysconfdir	/etc/php4
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	PHP language bindings for GTK+ toolkit
Summary(pl):	Modu� PHP z wi�zaniami do GTK+
Name:		php4-gtk
Version:	1.0.2
Release:	5
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
BuildRequires:	php4-devel >= 4.3.0
BuildRequires:	php4-pcre >= 4.3.0
BuildRequires:	rpmbuild(macros) >= 1.254
%{?requires_php_extension}
Requires:	php4-cli
Obsoletes:	php-devel
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

%description -l pl
PHP-GTK jest rozszerzeniem PHP kt�re pozwala pisa� klienckie przeno�ne
aplikacje typu GUI. To jest pierwsze rozszerzenie tego typu i jednym z
cel�w kt�re przy�wieca�y jego autorom by�o pokazanie �e PHP jest
j�zykiem skryptowym og�lnego zastosowania, kt�ry pasuje do czego�
wi�cej ni� tylko aplikacje WWW.

To rozszerzenie _nie_pozwala_ na u�ywanie program�w korzystaj�cych z
GTK+ przez przegl�dark� i nie mo�e by� u�ywane w �rodowisku WWW. Jest
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
