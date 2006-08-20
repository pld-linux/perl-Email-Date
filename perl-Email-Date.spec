#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Date
Summary:	Email::Date - find and format Date headers
Summary(pl):	Email::Date - znajdywanie i formatowanie nag³ówków Date
Name:		perl-Email-Date
Version:	1.101
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	38019e955a23f1cdb9f94e37000c87b8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Abstract >= 2.10
BuildRequires:	perl-Email-Simple >= 1.9
BuildRequires:	perl-Test-Pod >= 1.14
BuildRequires:	perl-Test-Pod-Coverage >= 1.08
BuildRequires:	perl-TimeDate >= 2.27
BuildRequires:	perl-Time-Piece >= 1.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RFC 2822 defines the Date: header. It declares the header a required
part of an email message. The syntax for date headers is clearly laid
out. Still, even a perfectly planned world has storms. The truth is,
many programs get it wrong. Very wrong. Or, they don't include a Date:
header at all. This often forces you to look elsewhere for the date,
and hoping to find something.

For this reason, the tedious process of looking for a valid date has
been encapsulated in this software. Further, the process of creating
RFC compliant date strings is also found in this software.

%description -l pl
RFC 2822 definiuje nag³ówek Date: (zawieraj±cy datê). Okre¶la ten
nag³ówek jako obowi±zkow± czê¶æ listu. Sk³adnia nag³ówków daty jest
jasno opisana. Mimo to wiele programów ¼le tworzy ten nag³ówek. Bardzo
¼le. Albo nie do³±cza go w ogóle. Zwykle zmusza to do szukania daty
gdzie¶ indziej z nadziej± znalezienia czego¶.

Z tego powodu nudny proces poszukiwania poprawnej daty zosta³
opakowany w ten pakiet. Co wiêcej, proces tworzenia ³añcuchów daty
zgodnych z RFC tak¿e mo¿na tu znale¼æ.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Email/*.pm
%{_mandir}/man3/*
