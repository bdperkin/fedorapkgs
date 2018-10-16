# Created by pyp2rpm-2.0.0
%global pypi_name cffi

Name:           python-%{pypi_name}
Version:        1.11.5
Release:        1%{?dist}
Summary:        Foreign Function Interface for Python calling C code

License:        MIT
URL:            http://cffi.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/e7/a7/4cd50e57cc6f436f1cc3a7e8fa700ff9b8b4d471620629074913e3735fb2/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

%description

CFFI
====

Foreign Function Interface for Python calling C code.
Please see
the `Documentation <http://cffi.readthedocs.org/>`_.

Contact
-------

`Mailing
list <https://groups.google.com/forum/#!forum/python-cffi>`_

%package -n     python3-%{pypi_name}
Summary:        Foreign Function Interface for Python calling C code
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-setuptools
%description -n python3-%{pypi_name}

CFFI
====

Foreign Function Interface for Python calling C code.
Please see
the `Documentation <http://cffi.readthedocs.org/>`_.

Contact
-------

`Mailing
list <https://groups.google.com/forum/#!forum/python-cffi>`_

%package -n python-%{pypi_name}-doc
Summary:        cffi documentation
%description -n python-%{pypi_name}-doc
Documentation for cffi

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.md LICENSE
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 1.11.5-1
- Initial package.