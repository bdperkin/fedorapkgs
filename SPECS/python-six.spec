# Created by pyp2rpm-2.0.0
%global pypi_name six

Name:           python-%{pypi_name}
Version:        1.11.0
Release:        1%{?dist}
Summary:        Python 2 and 3 compatibility utilities

License:        MIT
URL:            http://pypi.python.org/pypi/six/
Source0:        https://files.pythonhosted.org/packages/16/d8/bc6316cf98419719bd59c91742194c111b6f2e85abac88e496adefaf7afe/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx

%description
.. image:: http://img.shields.io/pypi/v/six.svg
   :target:
https://pypi.python.org/pypi/six

.. image:: https://travis-
ci.org/benjaminp/six.svg?branch=master
    :target: https://travis-
ci.org/benjaminp/six

.. image:: http://img.shields.io/badge/license-MIT-
green.svg
   :target: https://github.com/benjaminp/six/blob/master/LICENSE

Six
is a Python 2 and 3 compatibility library.  It provides ...

%package -n     python3-%{pypi_name}
Summary:        Python 2 and 3 compatibility utilities
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
.. image:: http://img.shields.io/pypi/v/six.svg
   :target:
https://pypi.python.org/pypi/six

.. image:: https://travis-
ci.org/benjaminp/six.svg?branch=master
    :target: https://travis-
ci.org/benjaminp/six

.. image:: http://img.shields.io/badge/license-MIT-
green.svg
   :target: https://github.com/benjaminp/six/blob/master/LICENSE

Six
is a Python 2 and 3 compatibility library.  It provides ...

%package -n python-%{pypi_name}-doc
Summary:        six documentation
%description -n python-%{pypi_name}-doc
Documentation for six

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
sphinx-build-3 documentation html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst LICENSE
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 1.11.0-1
- Initial package.