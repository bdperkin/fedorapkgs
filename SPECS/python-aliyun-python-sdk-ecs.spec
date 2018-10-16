# Created by pyp2rpm-2.0.0
%global pypi_name aliyun-python-sdk-ecs

Name:           python-%{pypi_name}
Version:        4.12.0
Release:        1%{?dist}
Summary:        The ecs module of Aliyun Python sdk

License:        Apache 2.0
URL:            http://develop.aliyun.com/sdk/python
Source0:        https://files.pythonhosted.org/packages/27/ee/82551878e5f98883e79449c888cb2880d44de6469d7770a79c0bea524466/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
aliyun-python-sdk-ecs
This is the ecs module of Aliyun Python SDK.

Aliyun
Python SDK is the official software development kit. It makes things easy to
integrate your Python application, library, or script with Aliyun services.
This module works on Python versions:

2.6.5 and greater
Documentation:

Please
visit http://develop.aliyun.com/sdk/python

%package -n     python3-%{pypi_name}
Summary:        The ecs module of Aliyun Python sdk
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
aliyun-python-sdk-ecs
This is the ecs module of Aliyun Python SDK.

Aliyun
Python SDK is the official software development kit. It makes things easy to
integrate your Python application, library, or script with Aliyun services.
This module works on Python versions:

2.6.5 and greater
Documentation:

Please
visit http://develop.aliyun.com/sdk/python

%package -n     python2-%{pypi_name}
Summary:        The ecs module of Aliyun Python sdk
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
aliyun-python-sdk-ecs
This is the ecs module of Aliyun Python SDK.

Aliyun
Python SDK is the official software development kit. It makes things easy to
integrate your Python application, library, or script with Aliyun services.
This module works on Python versions:

2.6.5 and greater
Documentation:

Please
visit http://develop.aliyun.com/sdk/python


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
%{python3_sitelib}/aliyun_python_sdk_ecs
%{python3_sitelib}/aliyun_python_sdk_ecs-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst
%{python2_sitelib}/aliyun_python_sdk_ecs
%{python2_sitelib}/aliyun_python_sdk_ecs-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 4.12.0-1
- Initial package.