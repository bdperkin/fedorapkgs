# Created by pyp2rpm-2.0.0
%global pypi_name openstacksdk

Name:           python-%{pypi_name}
Version:        0.17.2
Release:        1%{?dist}
Summary:        An SDK for building applications to work with OpenStack

License:        ASL %(TODO: version)s
URL:            http://developer.openstack.org/sdks/python/openstacksdk/
Source0:        https://files.pythonhosted.org/packages/cd/2b/0d42cceb14204f90c567fa3244468bd2611ae2cad3117311bdba93b766a1/%{pypi_name}-%{version}.tar.gz
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
openstacksdk
============

openstacksdk is a client library for building
applications to work
with OpenStack clouds. The project aims to provide a
consistent and
complete set of interactions with OpenStack's many services,
along with
complete documentation, examples, and tools.

It also contains an
abstraction interface layer. Clouds can do many things, but
there are probably
only about 10 of ...

%package -n     python3-%{pypi_name}
Summary:        An SDK for building applications to work with OpenStack
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
openstacksdk
============

openstacksdk is a client library for building
applications to work
with OpenStack clouds. The project aims to provide a
consistent and
complete set of interactions with OpenStack's many services,
along with
complete documentation, examples, and tools.

It also contains an
abstraction interface layer. Clouds can do many things, but
there are probably
only about 10 of ...

%package -n     python2-%{pypi_name}
Summary:        An SDK for building applications to work with OpenStack
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
openstacksdk
============

openstacksdk is a client library for building
applications to work
with OpenStack clouds. The project aims to provide a
consistent and
complete set of interactions with OpenStack's many services,
along with
complete documentation, examples, and tools.

It also contains an
abstraction interface layer. Clouds can do many things, but
there are probably
only about 10 of ...

%package -n python-%{pypi_name}-doc
Summary:        openstacksdk documentation
%description -n python-%{pypi_name}-doc
Documentation for openstacksdk

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
%doc README.rst openstack/tests/ansible/README.txt LICENSE
%{python3_sitelib}/ 
%{python3_sitelib}/openstack
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst openstack/tests/ansible/README.txt LICENSE
%{python2_sitelib}/ 
%{python2_sitelib}/openstack
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 0.17.2-1
- Initial package.