%define real_name Crypt-UnixCrypt

Summary:	Crypt-UnixCrypt module for perl 
Name:		perl-%{real_name}
Version:	1.0
Release:	8
License:	GPL or Artistic
Group:		Development/Perl
URL:		https://search.cpan.org/dist/%{real_name}
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




%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1.0-6mdv2011.0
+ Revision: 680871
- mass rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 1.0-5mdv2011.0
+ Revision: 430398
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0-4mdv2009.0
+ Revision: 256381
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0-2mdv2008.1
+ Revision: 136971
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Wed Sep 13 2006 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdv2007.0
- rebuild

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.0-1mdk
- initial Mandriva package

