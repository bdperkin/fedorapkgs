# Created by pyp2rpm-2.0.0
%global pypi_name google-auth

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Google Authentication Library

License:        ASL %(TODO: version)s
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python
Source0:        https://files.pythonhosted.org/packages/7e/cd/dae5c39974b040741215ed346263152c93af21a22dc124c7ad451fbee417/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
Google Auth Python Library
==========================

|build| |docs| |pypi|
This library simplifies using Google's various server-to-server authentication
mechanisms to access Google APIs.

.. |build| image:: https://travis-
ci.org/GoogleCloudPlatform/google-auth-library-python.svg?branch=master
:target: https://travis-ci.org/GoogleCloudPlatform/google-auth-library-python
.. |docs| image:: ...

%package -n     python3-%{pypi_name}
Summary:        Google Authentication Library
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Google Auth Python Library
==========================

|build| |docs| |pypi|
This library simplifies using Google's various server-to-server authentication
mechanisms to access Google APIs.

.. |build| image:: https://travis-
ci.org/GoogleCloudPlatform/google-auth-library-python.svg?branch=master
:target: https://travis-ci.org/GoogleCloudPlatform/google-auth-library-python
.. |docs| image:: ...

%package -n     python2-%{pypi_name}
Summary:        Google Authentication Library
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Google Auth Python Library
==========================

|build| |docs| |pypi|
This library simplifies using Google's various server-to-server authentication
mechanisms to access Google APIs.

.. |build| image:: https://travis-
ci.org/GoogleCloudPlatform/google-auth-library-python.svg?branch=master
:target: https://travis-ci.org/GoogleCloudPlatform/google-auth-library-python
.. |docs| image:: ...


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
%{python3_sitelib}/google_auth
%{python3_sitelib}/google_auth-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst LICENSE
%{python2_sitelib}/google_auth
%{python2_sitelib}/google_auth-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 1.5.1-1
- Initial package.