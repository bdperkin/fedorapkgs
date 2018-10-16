# Created by pyp2rpm-2.0.0
%global pypi_name netifaces

Name:           python-%{pypi_name}
Version:        0.10.7
Release:        1%{?dist}
Summary:        Portable network interface information

License:        MIT
URL:            https://github.com/al45tair/netifaces
Source0:        https://files.pythonhosted.org/packages/81/39/4e9a026265ba944ddf1fea176dbb29e0fe50c43717ba4fcf3646d099fe38/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
netifaces 0.10.7
================

+-------------+------------------+
|
Linux/macOS | |BuildStatus|    |
+-------------+------------------+
| Windows
| |WinBuildStatus| |
+-------------+------------------+

.. |BuildStatus|
image:: https://travis-ci.org/al45tair/netifaces.svg?branch=master
   :target:
https://travis-ci.org/al45tair/dmgbuild
   :alt: Build Status (Linux/Mac)

..
...

%package -n     python3-%{pypi_name}
Summary:        Portable network interface information
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
netifaces 0.10.7
================

+-------------+------------------+
|
Linux/macOS | |BuildStatus|    |
+-------------+------------------+
| Windows
| |WinBuildStatus| |
+-------------+------------------+

.. |BuildStatus|
image:: https://travis-ci.org/al45tair/netifaces.svg?branch=master
   :target:
https://travis-ci.org/al45tair/dmgbuild
   :alt: Build Status (Linux/Mac)

..
...

%package -n     python2-%{pypi_name}
Summary:        Portable network interface information
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
netifaces 0.10.7
================

+-------------+------------------+
|
Linux/macOS | |BuildStatus|    |
+-------------+------------------+
| Windows
| |WinBuildStatus| |
+-------------+------------------+

.. |BuildStatus|
image:: https://travis-ci.org/al45tair/netifaces.svg?branch=master
   :target:
https://travis-ci.org/al45tair/dmgbuild
   :alt: Build Status (Linux/Mac)

..
...


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
%doc README.rst
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 0.10.7-1
- Initial package.