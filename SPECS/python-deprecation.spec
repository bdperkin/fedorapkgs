# Created by pyp2rpm-2.0.0
%global pypi_name deprecation

Name:           python-%{pypi_name}
Version:        2.0.6
Release:        1%{?dist}
Summary:        A library to handle automated deprecations

License:        ASL %(TODO: version)s
URL:            http://deprecation.readthedocs.io/
Source0:        https://files.pythonhosted.org/packages/cd/35/ab3995718c7b12d6a5e69f40540fe1df0b505cca5ee6af169d23ab9d0b00/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
deprecation
===========

.. image::
https://readthedocs.org/projects/deprecation/badge/?version=latest
   :target:
http://deprecation.readthedocs.io/en/latest/
   :alt: Documentation Status

..
image:: https://travis-ci.org/briancurtin/deprecation.svg?branch=master
:target: https://travis-ci.org/briancurtin/deprecation

.. image:: ...

%package -n     python3-%{pypi_name}
Summary:        A library to handle automated deprecations
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-packaging
%description -n python3-%{pypi_name}
deprecation
===========

.. image::
https://readthedocs.org/projects/deprecation/badge/?version=latest
   :target:
http://deprecation.readthedocs.io/en/latest/
   :alt: Documentation Status

..
image:: https://travis-ci.org/briancurtin/deprecation.svg?branch=master
:target: https://travis-ci.org/briancurtin/deprecation

.. image:: ...

%package -n     python2-%{pypi_name}
Summary:        A library to handle automated deprecations
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-packaging
%description -n python2-%{pypi_name}
deprecation
===========

.. image::
https://readthedocs.org/projects/deprecation/badge/?version=latest
   :target:
http://deprecation.readthedocs.io/en/latest/
   :alt: Documentation Status

..
image:: https://travis-ci.org/briancurtin/deprecation.svg?branch=master
:target: https://travis-ci.org/briancurtin/deprecation

.. image:: ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%py2_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst LICENSE
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst LICENSE

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.0.6-1
- Initial package.