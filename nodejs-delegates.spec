%{?scl:%scl_package nodejs-delegates}
%{!?scl:%global pkg_name %{name}}

# spec file for package nodejs-nodejs-delegates

%global npm_name delegates
%{?nodejs_find_provides_and_requires}

%global enable_tests 0

Name:		%{?scl_prefix}nodejs-delegates
Version:	1.0.0
Release:	1%{?dist}
Summary:	Delegate methods and accessors to another property
Url:		https://github.com/visionmedia/node-delegates
Source0:	https://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
License:	MIT

BuildArch:	noarch

%if 0%{?fedora} >= 19
ExclusiveArch: %{nodejs_arches} noarch
%else
ExclusiveArch: %{ix86} x86_64 %{arm} noarch
%endif

BuildRequires:  %{?scl_prefix}nodejs-devel
BuildRequires:  %{?scl_prefix}runtime
%if 0%{?enable_tests}
BuildRequires:	%{?scl_prefix}npm(mocha)
BuildRequires:	%{?scl_prefix}npm(should)
%endif

%description
delegate methods and accessors to another property

%prep
%setup -q -n package

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

%doc Readme.md License

%changelog
* Thu Feb 11 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.0.0-1
- New upstream release

* Tue Dec 01 2015 Tomas Hrcka <thrcka@redhat.com> - 0.1.0-1
- Initial build
