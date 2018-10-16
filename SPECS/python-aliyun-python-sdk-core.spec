# Created by pyp2rpm-2.0.0
%global pypi_name aliyun-python-sdk-core

Name:           python-%{pypi_name}
Version:        2.9.5
Release:        1%{?dist}
Summary:        The core module of Aliyun Python SDK

License:        Apache 2.0
URL:            http://develop.aliyun.com/sdk/python
Source0:        https://files.pythonhosted.org/packages/ca/89/834d50f84329123b3d77c68591569e126d427a8bcd6004edb426ab438c51/%{pypi_name}-%{version}.tar.gz
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

   * 2.6.5 and greater


   Documentation:

   Please visit
...

%package -n     python3-%{pypi_name}
Summary:        The core module of Aliyun Python SDK
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

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

   * 2.6.5 and greater


   Documentation:

   Please visit
...

%package -n     python2-%{pypi_name}
Summary:        The core module of Aliyun Python SDK
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

   * 2.6.5 and greater


   Documentation:

   Please visit
...


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
%py2_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%py3_install


%files -n python3-%{pypi_name} 
%doc 
%{python3_sitelib}/aliyun_python_sdk_core
%{python3_sitelib}/aliyun_python_sdk_core-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc 
%{python2_sitelib}/aliyun_python_sdk_core
%{python2_sitelib}/aliyun_python_sdk_core-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.9.5-1
- Initial package.