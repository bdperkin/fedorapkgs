# Created by pyp2rpm-2.0.0
%global pypi_name jsonpatch

Name:           python-%{pypi_name}
Version:        1.23
Release:        1%{?dist}
Summary:        Apply JSON-Patches (RFC 6902)

License:        BSD
URL:            https://github.com/stefankoegl/python-json-patch
Source0:        https://files.pythonhosted.org/packages/9a/7d/bcf203d81939420e1aaf7478a3efce1efb8ccb4d047a33cb85d7f96d775e/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
python-json-patch
=================

|PyPI version| |Supported Python versions|
|Build Status| |Coverage
Status|

Applying JSON Patches in Python
-------------------------------

Library to apply JSON Patches according to
`RFC
6902 <http://tools.ietf.org/html/rfc6902>`__

See source code for examples
-  Website: https://github.com/stefankoegl/python-json-patch
-  Repository: ...

%package -n     python3-%{pypi_name}
Summary:        Apply JSON-Patches (RFC 6902)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
python-json-patch
=================

|PyPI version| |Supported Python versions|
|Build Status| |Coverage
Status|

Applying JSON Patches in Python
-------------------------------

Library to apply JSON Patches according to
`RFC
6902 <http://tools.ietf.org/html/rfc6902>`__

See source code for examples
-  Website: https://github.com/stefankoegl/python-json-patch
-  Repository: ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
cp %{buildroot}/%{_bindir}/jsondiff %{buildroot}/%{_bindir}/jsondiff-3
ln -sf %{_bindir}/jsondiff-3 %{buildroot}/%{_bindir}/jsondiff-%{python3_version}
cp %{buildroot}/%{_bindir}/jsonpatch %{buildroot}/%{_bindir}/jsonpatch-3
ln -sf %{_bindir}/jsonpatch-3 %{buildroot}/%{_bindir}/jsonpatch-%{python3_version}


%files -n python3-%{pypi_name} 
%doc README.md
%{_bindir}/jsondiff
%{_bindir}/jsondiff-3
%{_bindir}/jsondiff-%{python3_version}
%{_bindir}/jsonpatch
%{_bindir}/jsonpatch-3
%{_bindir}/jsonpatch-%{python3_version}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 1.23-1
- Initial package.