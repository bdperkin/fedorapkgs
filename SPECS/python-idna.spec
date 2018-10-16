# Created by pyp2rpm-2.0.0
%global pypi_name idna

Name:           python-%{pypi_name}
Version:        2.7
Release:        1%{?dist}
Summary:        Internationalized Domain Names in Applications (IDNA)

License:        BSD
URL:            https://github.com/kjd/idna
Source0:        https://files.pythonhosted.org/packages/65/c4/80f97e9c9628f3cac9b98bfca0402ede54e0563b56482e3e6e45c43c4935/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Internationalized Domain Names in Applications (IDNA)
=====================================================

Support for the
Internationalised Domain Names in Applications
(IDNA) protocol as specified in
`RFC 5891 <http://tools.ietf.org/html/rfc5891>`_.
This is the latest version of
the protocol and is sometimes referred to as
“IDNA 2008”.

This library also
provides support for Unicode Technical ...

%package -n     python3-%{pypi_name}
Summary:        Internationalized Domain Names in Applications (IDNA)
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Internationalized Domain Names in Applications (IDNA)
=====================================================

Support for the
Internationalised Domain Names in Applications
(IDNA) protocol as specified in
`RFC 5891 <http://tools.ietf.org/html/rfc5891>`_.
This is the latest version of
the protocol and is sometimes referred to as
“IDNA 2008”.

This library also
provides support for Unicode Technical ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst LICENSE.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.7-1
- Initial package.