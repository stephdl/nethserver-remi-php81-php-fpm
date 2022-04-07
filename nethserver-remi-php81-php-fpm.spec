Name: nethserver-remi-php81-php-fpm
Version: 1.0.0
Release: 1%{?dist}
Summary: NethServer remi-php81-php-fpm configuration
License: GPL
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

BuildRequires: nethserver-devtools

Requires: php81, php81-php-fpm
Requires: php81-php-bcmath, php81-php-gd, php81-php-imap
Requires: php81-php-ldap, php81-php-enchant, php81-php-mbstring
Requires: php81-php-pdo, php81-php-tidy, php81-php-mysqlnd
Requires: php81-php-soap, php81-php-pgsql
Requires: php81-php-pecl-apcu, php81-php-intl
Requires: php81-php-opcache
# specific dependencies from remi to get same PHP modules list of RH SCL
Requires: php81-php-xml, php81-php-pecl-zip, php81-php-process

%description
Basic support for PHP 81 using SCL of remi repository

%prep
%setup -q

%build
%{makedocs}
perl createlinks

%install
rm -rf %{buildroot}
(cd root ; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-%{release}-filelist


%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
%dir %{_nseventsdir}/%{name}-update


%changelog
* Thu Apr 07 2022 stephane de Labrusse <stephdl
- Initial release

* Fri Dec 18 2020 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.0-1
- PHP81 SCL from remi  - NethServer/dev#6356

* Mon Dec 07 2020 Stephane de Labrusse <stephdl@de-labrusse.fr> - 1.0.0-1
- Initial release of PHP81 for NethServer
