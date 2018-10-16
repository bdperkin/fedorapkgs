# Created by pyp2rpm-2.0.0
%global pypi_name pbr

Name:           python-%{pypi_name}
Version:        4.3.0
Release:        1%{?dist}
Summary:        Python Build Reasonableness

License:        Apache 2.0
URL:            https://docs.openstack.org/pbr/latest/
Source0:        https://files.pythonhosted.org/packages/4c/22/91722b7d842a9e2e6ae41346f691fea95d9ac08678de7ac51c38754f9961/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr
BuildRequires:  python3-sphinx

%description
Introduction
============

.. image:: https://img.shields.io/pypi/v/pbr.svg
:target: https://pypi.python.org/pypi/pbr/
    :alt: Latest Version

.. image::
https://img.shields.io/pypi/dm/pbr.svg
    :target:
https://pypi.python.org/pypi/pbr/
    :alt: Downloads

PBR is a library that
injects some useful and sensible default behaviors
into your setuptools run. It
started off life as the chunks ...

%package -n     python3-%{pypi_name}
Summary:        Python Build Reasonableness
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
Introduction
============

.. image:: https://img.shields.io/pypi/v/pbr.svg
:target: https://pypi.python.org/pypi/pbr/
    :alt: Latest Version

.. image::
https://img.shields.io/pypi/dm/pbr.svg
    :target:
https://pypi.python.org/pypi/pbr/
    :alt: Downloads

PBR is a library that
injects some useful and sensible default behaviors
into your setuptools run. It
started off life as the chunks ...

%package -n python-%{pypi_name}-doc
Summary:        pbr documentation
%description -n python-%{pypi_name}-doc
Documentation for pbr

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
sphinx-build-3 pbr/tests/testpackage/doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst pbr/tests/testpackage/README.txt pbr/tests/testpackage/LICENSE.txt LICENSE
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 4.3.0-1
- Initial package.