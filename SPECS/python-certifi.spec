# Created by pyp2rpm-2.0.0
%global pypi_name certifi

Name:           python-%{pypi_name}
Version:        2018.10.15
Release:        1%{?dist}
Summary:        Python package for providing Mozilla's CA Bundle

License:        MPLv2.0
URL:            http://certifi.io/
Source0:        https://files.pythonhosted.org/packages/41/b6/4f0cefba47656583217acd6cd797bc2db1fede0d53090fdc28ad2c8e0716/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
Certifi: Python SSL Certificates
================================

`Certifi`_
is a carefully curated collection of Root Certificates for
validating the
trustworthiness of SSL certificates while verifying the identity
of TLS hosts.
It has been extracted from the `Requests`_ project.

Installation
------------
``certifi`` is available on PyPI. Simply install it with ``pip``::

    $ pip
install ...

%package -n     python3-%{pypi_name}
Summary:        Python package for providing Mozilla's CA Bundle
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Certifi: Python SSL Certificates
================================

`Certifi`_
is a carefully curated collection of Root Certificates for
validating the
trustworthiness of SSL certificates while verifying the identity
of TLS hosts.
It has been extracted from the `Requests`_ project.

Installation
------------
``certifi`` is available on PyPI. Simply install it with ``pip``::

    $ pip
install ...

%package -n     python2-%{pypi_name}
Summary:        Python package for providing Mozilla's CA Bundle
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Certifi: Python SSL Certificates
================================

`Certifi`_
is a carefully curated collection of Root Certificates for
validating the
trustworthiness of SSL certificates while verifying the identity
of TLS hosts.
It has been extracted from the `Requests`_ project.

Installation
------------
``certifi`` is available on PyPI. Simply install it with ``pip``::

    $ pip
install ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%py2_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2018.10.15-1
- Initial package.