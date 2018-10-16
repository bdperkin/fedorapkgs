# Created by pyp2rpm-2.0.0
%global pypi_name jsonpointer

Name:           python-%{pypi_name}
Version:        2.0
Release:        1%{?dist}
Summary:        Identify specific nodes in a JSON document (RFC 6901)

License:        BSD
URL:            https://github.com/stefankoegl/python-json-pointer
Source0:        https://files.pythonhosted.org/packages/52/e7/246d9ef2366d430f0ce7bdc494ea2df8b49d7a2a41ba51f5655f68cfe85f/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
python-json-pointer
===================

|PyPI version| |Supported Python
versions| |Build Status| |Coverage
Status|

Resolve JSON Pointers in Python
-------------------------------

Library to resolve JSON Pointers according to
`RFC
6901 <http://tools.ietf.org/html/rfc6901>`__

See source code for examples
\* Website:
https://github.com/stefankoegl/python-json-pointer \* ...

%package -n     python3-%{pypi_name}
Summary:        Identify specific nodes in a JSON document (RFC 6901)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
python-json-pointer
===================

|PyPI version| |Supported Python
versions| |Build Status| |Coverage
Status|

Resolve JSON Pointers in Python
-------------------------------

Library to resolve JSON Pointers according to
`RFC
6901 <http://tools.ietf.org/html/rfc6901>`__

See source code for examples
\* Website:
https://github.com/stefankoegl/python-json-pointer \* ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
cp %{buildroot}/%{_bindir}/jsonpointer %{buildroot}/%{_bindir}/jsonpointer-3
ln -sf %{_bindir}/jsonpointer-3 %{buildroot}/%{_bindir}/jsonpointer-%{python3_version}


%files -n python3-%{pypi_name} 
%doc README.md LICENSE.txt
%{_bindir}/jsonpointer
%{_bindir}/jsonpointer-3
%{_bindir}/jsonpointer-%{python3_version}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.0-1
- Initial package.