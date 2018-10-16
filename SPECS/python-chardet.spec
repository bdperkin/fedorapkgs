# Created by pyp2rpm-2.0.0
%global pypi_name chardet

Name:           python-%{pypi_name}
Version:        3.0.4
Release:        1%{?dist}
Summary:        Universal encoding detector for Python 2 and 3

License:        LGPL
URL:            https://github.com/chardet/chardet
Source0:        https://files.pythonhosted.org/packages/fc/bb/a5768c230f9ddb03acc9ef3f0d4a3cf93462473795d18e9535498c8f929d/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-hypothesis
BuildRequires:  python3-sphinx

%description
Chardet: The Universal Character Encoding Detector
--------------------------------------------------

.. image::
https://img.shields.io/travis/chardet/chardet/stable.svg
   :alt: Build status
:target: https://travis-ci.org/chardet/chardet

.. image::
https://img.shields.io/coveralls/chardet/chardet/stable.svg
   :target:
https://coveralls.io/r/chardet/chardet

.. image:: ...

%package -n     python3-%{pypi_name}
Summary:        Universal encoding detector for Python 2 and 3
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
 
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
Chardet: The Universal Character Encoding Detector
--------------------------------------------------

.. image::
https://img.shields.io/travis/chardet/chardet/stable.svg
   :alt: Build status
:target: https://travis-ci.org/chardet/chardet

.. image::
https://img.shields.io/coveralls/chardet/chardet/stable.svg
   :target:
https://coveralls.io/r/chardet/chardet

.. image:: ...

%package -n python-%{pypi_name}-doc
Summary:        chardet documentation
%description -n python-%{pypi_name}-doc
Documentation for chardet

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


%files -n python3-%{pypi_name} 
%doc docs/README.md README.rst tests/README.txt LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 3.0.4-1
- Initial package.