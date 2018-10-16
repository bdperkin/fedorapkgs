# Created by pyp2rpm-2.0.0
%global pypi_name stevedore

Name:           python-%{pypi_name}
Version:        1.29.0
Release:        1%{?dist}
Summary:        Manage dynamic plugins for Python applications

License:        ASL %(TODO: version)s
URL:            https://docs.openstack.org/stevedore/latest/
Source0:        https://files.pythonhosted.org/packages/61/c9/1d10fc4ffd9657caea9e3f0428cad6e0eefed9dfea11435f97ab34c1927f/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr >= 2.0.0
BuildRequires:  python3-sphinx
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr >= 2.0.0
BuildRequires:  python-sphinx

%description
===========================================================
stevedore -- Manage
dynamic plugins for Python applications
===========================================================

.. image::
https://img.shields.io/pypi/v/stevedore.svg
    :target:
https://pypi.org/project/stevedore/
    :alt: Latest Version

.. image::
https://img.shields.io/pypi/dm/stevedore.svg
    :target: ...

%package -n     python3-%{pypi_name}
Summary:        Manage dynamic plugins for Python applications
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
===========================================================
stevedore -- Manage
dynamic plugins for Python applications
===========================================================

.. image::
https://img.shields.io/pypi/v/stevedore.svg
    :target:
https://pypi.org/project/stevedore/
    :alt: Latest Version

.. image::
https://img.shields.io/pypi/dm/stevedore.svg
    :target: ...

%package -n     python2-%{pypi_name}
Summary:        Manage dynamic plugins for Python applications
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
===========================================================
stevedore -- Manage
dynamic plugins for Python applications
===========================================================

.. image::
https://img.shields.io/pypi/v/stevedore.svg
    :target:
https://pypi.org/project/stevedore/
    :alt: Latest Version

.. image::
https://img.shields.io/pypi/dm/stevedore.svg
    :target: ...

%package -n python-%{pypi_name}-doc
Summary:        stevedore documentation
%description -n python-%{pypi_name}-doc
Documentation for stevedore

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%py2_build
# generate html docs 
sphinx-build-3 doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst LICENSE
%{python3_sitelib}/ 
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst LICENSE
%{python2_sitelib}/ 
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 1.29.0-1
- Initial package.