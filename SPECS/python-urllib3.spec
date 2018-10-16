# Created by pyp2rpm-2.0.0
%global pypi_name urllib3

Name:           python-%{pypi_name}
Version:        1.23
Release:        1%{?dist}
Summary:        HTTP library with thread-safe connection pooling, file post, and more

License:        MIT
URL:            https://urllib3.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/3c/d2/dc5471622bd200db1cd9319e02e71bc655e9ea27b8e0ce65fc69de0dac15/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  python3-tornado
BuildRequires:  python3-sphinx

%description
urllib3
=======

.. image:: https://travis-
ci.org/urllib3/urllib3.svg?branch=master
        :alt: Build status on Travis
:target: https://travis-ci.org/urllib3/urllib3

.. image::
https://img.shields.io/appveyor/ci/urllib3/urllib3/master.svg
        :alt:
Build status on AppVeyor
        :target:
https://ci.appveyor.com/project/urllib3/urllib3

.. image:: ...

%package -n     python3-%{pypi_name}
Summary:        HTTP library with thread-safe connection pooling, file post, and more
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
urllib3
=======

.. image:: https://travis-
ci.org/urllib3/urllib3.svg?branch=master
        :alt: Build status on Travis
:target: https://travis-ci.org/urllib3/urllib3

.. image::
https://img.shields.io/appveyor/ci/urllib3/urllib3/master.svg
        :alt:
Build status on AppVeyor
        :target:
https://ci.appveyor.com/project/urllib3/urllib3

.. image:: ...

%package -n python-%{pypi_name}-doc
Summary:        urllib3 documentation
%description -n python-%{pypi_name}-doc
Documentation for urllib3

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install


%check
%{__python3} setup.py test

%files -n python3-%{pypi_name} 
%doc dummyserver/certs/README.rst README.rst LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 1.23-1
- Initial package.