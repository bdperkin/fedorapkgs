# Created by pyp2rpm-2.0.0
%global pypi_name os-service-types

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Python library for consuming OpenStack sevice-types-authority data

License:        Apache 2.0
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/a2/bc/c8bc9cce8ec064558ae9b8ab2dbea9d5bdfbaf5c50f637a19cb120410b10/%{pypi_name}-%{version}.tar.gz
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
================
os-service-types
================

Python library for
consuming OpenStack sevice-types-authority data

The `OpenStack Service Types
Authority`_ contains information about official
OpenStack services and their
historical ``service-type`` aliases.

The data is in JSON and the latest data
should always be used. This simple
library exists to allow for easy consumption
of the data, ...

%package -n     python3-%{pypi_name}
Summary:        Python library for consuming OpenStack sevice-types-authority data
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
================
os-service-types
================

Python library for
consuming OpenStack sevice-types-authority data

The `OpenStack Service Types
Authority`_ contains information about official
OpenStack services and their
historical ``service-type`` aliases.

The data is in JSON and the latest data
should always be used. This simple
library exists to allow for easy consumption
of the data, ...

%package -n     python2-%{pypi_name}
Summary:        Python library for consuming OpenStack sevice-types-authority data
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
================
os-service-types
================

Python library for
consuming OpenStack sevice-types-authority data

The `OpenStack Service Types
Authority`_ contains information about official
OpenStack services and their
historical ``service-type`` aliases.

The data is in JSON and the latest data
should always be used. This simple
library exists to allow for easy consumption
of the data, ...

%package -n python-%{pypi_name}-doc
Summary:        os-service-types documentation
%description -n python-%{pypi_name}-doc
Documentation for os-service-types

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
%doc doc/source/readme.rst README.rst LICENSE
%{python3_sitelib}/ 
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/os_service_types-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc doc/source/readme.rst README.rst LICENSE
%{python2_sitelib}/ 
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/os_service_types-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 1.3.0-1
- Initial package.