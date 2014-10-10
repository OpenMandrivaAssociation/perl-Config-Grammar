%define upstream_name    Config-Grammar
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5
Summary:	A grammar-based, user-friendly config parser
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Config::Grammar is a module to parse configuration files. The configuration
may consist of multiple-level sections with assignments and tabular data.
The parsed data will be returned as a hash containing the whole
configuration. Config::Grammar uses a grammar that is supplied upon
creation of a Config::Grammar object to parse the configuration file and
return helpful error messages in case of syntax errors. Using the *makepod*
method you can generate documentation of the configuration file format.

The *maketmpl* method can generate a template configuration file. If your
grammar contains regexp matches, the template will not be all that helpful
as Config::Grammar is not smart enough to give you sensible template data
based in regular expressions. The related function *maketmplmin* generates
a minimal configuration template without examples, regexps or comments and
thus allows an experienced user to fill in the configuration data more
efficiently.

Grammar Definition
    The grammar is a multiple-level hash of hashes, which follows the
    structure of the configuration. Each section or variable is represented
    by a hash with the same structure. Each hash contains special keys
    starting with an underscore such as '_sections', '_vars', '_sub' or
    '_re' to denote meta data with information about that section or
    variable. Other keys are used to structure the hash according to the
    same nesting structure of the configuration itself. The starting hash
    given as parameter to 'new' contains the "root section".

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.100.0-3mdv2011.0
+ Revision: 654898
- rebuild for updated spec-helper

* Wed Sep 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.0-2mdv2011.0
+ Revision: 443528
- backportability fix

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 1.100.0-1mdv2010.0
+ Revision: 409026
- rebuild using %%perl_convert_version
- rebuild

* Mon May 04 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.10-1mdv2010.0
+ Revision: 371910
- import perl-Config-Grammar


* Mon May 04 2009 cpan2dist 1.10-1mdv
- initial mdv release, generated with cpan2dist
