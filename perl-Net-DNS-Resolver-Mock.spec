#
# Conditional build:
%bcond_with	tests		# perform "make test"
#
%define		pdir	Net
%define		pnam	DNS-Resolver-Mock
Summary:	Net::DNS::Resolver::Mock - Mock a DNS Resolver object for testing
Name:		perl-Net-DNS-Resolver-Mock
Version:	1.20230216
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Net/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d191b6b1eb40497024988f500fe65ed4
URL:		https://metacpan.org/release/Net-DNS-Resolver-Mock/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Net-DNS
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A subclass of Net::DNS::Resolver which parses a zonefile for it's data
source. Primarily for use in testing.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/Net/DNS/Resolver/*.pm
%{_mandir}/man3/*
