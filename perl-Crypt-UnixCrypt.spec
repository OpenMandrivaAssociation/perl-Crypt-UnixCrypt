%define real_name Crypt-UnixCrypt

Summary:	Crypt-UnixCrypt module for perl 
Name:		perl-%{real_name}
Version:	1.0
Release:	%mkrel 5
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module is for all those poor souls whose perl port answers to the
use of crypt() with the message `The crypt() function is unimplemented
due to excessive paranoia.'.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES README
%{perl_vendorlib}/Crypt/UnixCrypt.pm
%{_mandir}/*/*


