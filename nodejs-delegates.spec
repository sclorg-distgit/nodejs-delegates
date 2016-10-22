%{?scl:%scl_package nodejs-delegates}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-delegates

%global npm_name delegates
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-delegates
Version:	0.1.0
Release:	4%{?dist}
Summary:	Delegate methods and accessors to another property
Url:		https://github.com/visionmedia/node-delegates
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
Source1:    https://raw.githubusercontent.com/tj/node-delegates/1.0.0/License
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}nodejs-devel
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(mocha)
BuildRequires:	%{?scl_prefix}npm(should)
%endif

%description
delegate methods and accessors to another property

%prep
%setup -q -n package

cp -p %{SOURCE1} .

rm -rf node_modules

%build

#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}

cp -pr package.json *.js \
%{buildroot}%{nodejs_sitelib}/%{npm_name}

%{nodejs_symlink_deps}

%if 0%{?enable_tests}

%check
%{nodejs_symlink_deps} --check

%endif

%files
%{nodejs_sitelib}/delegates

%doc Readme.md

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.0-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.0-3
- Rebuilt with updated metapackage

* Sat Feb 13 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.0-2
- Add License

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.0-1
- Initial build
