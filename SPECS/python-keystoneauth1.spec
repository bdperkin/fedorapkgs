# Created by pyp2rpm-2.0.0
%global pypi_name keystoneauth1

Name:           python-%{pypi_name}
Version:        3.11.0
Release:        1%{?dist}
Summary:        Authentication Library for OpenStack Identity

License:        ASL %(TODO: version)s
URL:            https://docs.openstack.org/keystoneauth/latest/
Source0:        https://files.pythonhosted.org/packages/0e/4c/d6738d1025949329bdf63428c9ac50a30a9c017038e97aac741b85c7563b/%{pypi_name}-%{version}.tar.gz
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
========================
Team and repository tags
========================

..
image:: https://governance.openstack.org/tc/badges/keystoneauth.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

..
Change things from this point on

============
keystoneauth
============

..
image:: https://img.shields.io/pypi/v/keystoneauth1.svg
    ...

%package -n     python3-%{pypi_name}
Summary:        Authentication Library for OpenStack Identity
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
========================
Team and repository tags
========================

..
image:: https://governance.openstack.org/tc/badges/keystoneauth.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

..
Change things from this point on

============
keystoneauth
============

..
image:: https://img.shields.io/pypi/v/keystoneauth1.svg
    ...

%package -n     python2-%{pypi_name}
Summary:        Authentication Library for OpenStack Identity
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
========================
Team and repository tags
========================

..
image:: https://governance.openstack.org/tc/badges/keystoneauth.svg
:target: https://governance.openstack.org/tc/reference/tags/index.html

..
Change things from this point on

============
keystoneauth
============

..
image:: https://img.shields.io/pypi/v/keystoneauth1.svg
    ...

%package -n python-%{pypi_name}-doc
Summary:        keystoneauth1 documentation
%description -n python-%{pypi_name}-doc
Documentation for keystoneauth1

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
* Tue Oct 16 2018 root - 3.11.0-1
- Initial package.