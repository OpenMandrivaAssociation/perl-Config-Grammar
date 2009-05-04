%define module   Config-Grammar
%define version    1.10
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A grammar-based, user-friendly config parser
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Config/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


