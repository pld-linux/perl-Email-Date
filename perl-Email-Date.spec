#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Email
%define	pnam	Date
Summary:	Email::Date - Find and Format Date Headers
#Summary(pl):	
Name:		perl-Email-Date
Version:	1.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	308f00689a06dcf73799c1f7d0d004c6
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Email-Simple >= 1.9
BuildRequires:	perl-TimeDate >= 2.27
BuildRequires:	perl-Time-Piece >= 1.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
RFC 2822 defines the C<Date:> header. It declares the header a required
part of an email message. The syntax for date headers is clearly laid
out. Stil, even a perfectly planned world has storms. The truth is, many
programs get it wrong. Very wrong. Or, they don't include a C<Date:>
header at all. This often forces you to look elsewhere for the date,
and hoping to find something.

For this reason, the tedious process of looking for a valid date has
been encapsulated in this software. Further, the process of creating
RFC compliant date strings is also found in this software.

# %description -l pl
# TODO

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
