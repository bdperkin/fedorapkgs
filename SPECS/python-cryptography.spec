# Created by pyp2rpm-2.0.0
%global pypi_name cryptography

Name:           python-%{pypi_name}
Version:        2.3.1
Release:        1%{?dist}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers

License:        ASL %(TODO: version)s and BSD
URL:            https://github.com/pyca/cryptography
Source0:        https://files.pythonhosted.org/packages/22/21/233e38f74188db94e8451ef6385754a98f3cad9b59bedf3a8e8b14988be4/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

%description
pyca/cryptography
=================

.. image::
https://img.shields.io/pypi/v/cryptography.svg
    :target:
https://pypi.org/project/cryptography/
    :alt: Latest Version

.. image::
https://readthedocs.org/projects/cryptography/badge/?version=latest
:target: https://cryptography.io
    :alt: Latest Docs

.. image:: https
://travis-ci.org/pyca/cryptography.svg?branch=master
    :target: ...

%package -n     python3-%{pypi_name}
Summary:        cryptography is a package which provides cryptographic recipes and primitives to Python developers
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-idna >= 2.1
Requires:       python3-asn1crypto >= 0.21.0
Requires:       python3-six >= 1.4.1
%description -n python3-%{pypi_name}
pyca/cryptography
=================

.. image::
https://img.shields.io/pypi/v/cryptography.svg
    :target:
https://pypi.org/project/cryptography/
    :alt: Latest Version

.. image::
https://readthedocs.org/projects/cryptography/badge/?version=latest
:target: https://cryptography.io
    :alt: Latest Docs

.. image:: https
://travis-ci.org/pyca/cryptography.svg?branch=master
    :target: ...

%package -n python-%{pypi_name}-doc
Summary:        cryptography documentation
%description -n python-%{pypi_name}-doc
Documentation for cryptography

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
%doc README.rst LICENSE LICENSE.APACHE LICENSE.BSD
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 2.3.1-1
- Initial package.