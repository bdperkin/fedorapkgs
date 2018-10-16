# Created by pyp2rpm-2.0.0
%global pypi_name requests

Name:           python-%{pypi_name}
Version:        2.19.1
Release:        1%{?dist}
Summary:        Python HTTP for Humans

License:        ASL %(TODO: version)s
URL:            http://python-requests.org
Source0:        https://files.pythonhosted.org/packages/54/1f/782a5734931ddf2e1494e4cd615a51ff98e1879cbe9eecbdfeaf09aa75e9/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Requests: HTTP for Humans
=========================

.. image::
https://img.shields.io/pypi/v/requests.svg
    :target:
https://pypi.org/project/requests/

.. image::
https://img.shields.io/pypi/l/requests.svg
    :target:
https://pypi.org/project/requests/

.. image::
https://img.shields.io/pypi/pyversions/requests.svg
    :target:
https://pypi.org/project/requests/

.. image:: ...

%package -n     python3-%{pypi_name}
Summary:        Python HTTP for Humans
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
Requests: HTTP for Humans
=========================

.. image::
https://img.shields.io/pypi/v/requests.svg
    :target:
https://pypi.org/project/requests/

.. image::
https://img.shields.io/pypi/l/requests.svg
    :target:
https://pypi.org/project/requests/

.. image::
https://img.shields.io/pypi/pyversions/requests.svg
    :target:
https://pypi.org/project/requests/

.. image:: ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.19.1-1
- Initial package.