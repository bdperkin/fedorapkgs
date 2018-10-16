# Created by pyp2rpm-2.0.0
%global pypi_name aliyun-python-sdk-core-v3

Name:           python-%{pypi_name}
Version:        2.9.4
Release:        1%{?dist}
Summary:        The core module of Aliyun Python3 SDK

License:        ASL %(TODO: version)s
URL:            http://develop.aliyun.com/sdk/python
Source0:        https://files.pythonhosted.org/packages/fe/d9/274971f9ba8c95b9959c5ce4b0d5572febd4bc6d622ecc1de7a3e861ad5a/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
======================
aliyun-python-sdk-core
======================


This is
the core module of Aliyun Python SDK.

Aliyun Python SDK is the official
software development kit. It makes things easy to integrate your Python
application,
library, or script with Aliyun services.

This module works on
Python versions:

   * 3.0.0 and greater


Documentation:

Please visit ...

%package -n     python3-%{pypi_name}
Summary:        The core module of Aliyun Python3 SDK
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
======================
aliyun-python-sdk-core
======================


This is
the core module of Aliyun Python SDK.

Aliyun Python SDK is the official
software development kit. It makes things easy to integrate your Python
application,
library, or script with Aliyun services.

This module works on
Python versions:

   * 3.0.0 and greater


Documentation:

Please visit ...

%package -n     python2-%{pypi_name}
Summary:        The core module of Aliyun Python3 SDK
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
======================
aliyun-python-sdk-core
======================


This is
the core module of Aliyun Python SDK.

Aliyun Python SDK is the official
software development kit. It makes things easy to integrate your Python
application,
library, or script with Aliyun services.

This module works on
Python versions:

   * 3.0.0 and greater


Documentation:

Please visit ...


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
%{python3_sitelib}/aliyun_python_sdk_core_v3
%{python3_sitelib}/aliyun_python_sdk_core_v3-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst
%{python2_sitelib}/aliyun_python_sdk_core_v3
%{python2_sitelib}/aliyun_python_sdk_core_v3-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.9.4-1
- Initial package.