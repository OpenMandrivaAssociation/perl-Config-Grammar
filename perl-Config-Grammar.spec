%define upstream_name    Config-Grammar
%define upstream_version 1.10

Name:       perl-%{upstream_name}
%if %mdkversion >= 201000
Version:    %perl_convert_version %{upstream_version}
%else
Version:    %{upstream_version}
%endif
Release:    %mkrel 2
Summary:    A grammar-based, user-friendly config parser
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

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
