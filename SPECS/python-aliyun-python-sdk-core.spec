# Created by pyp2rpm-3.3.2
%global pypi_name aliyun-python-sdk-core

Name:           python-%{pypi_name}
Version:        2.9.5
Release:        1%{?dist}
Summary:        The core module of Aliyun Python SDK

License:        Apache
URL:            http://develop.aliyun.com/sdk/python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)

%description
 aliyun-python-sdk-core This is the core module of Aliyun Python SDK.Aliyun
Python SDK is the official software development kit. It makes things easy to
integrate your Python application, library, or script with Aliyun services.This
module works on Python versions: * 2.6.5 and greater Documentation: Please
visit

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(pycryptodome) >= 3.4.7
%description -n python2-%{pypi_name}
 aliyun-python-sdk-core This is the core module of Aliyun Python SDK.Aliyun
Python SDK is the official software development kit. It makes things easy to
integrate your Python application, library, or script with Aliyun services.This
module works on Python versions: * 2.6.5 and greater Documentation: Please
visit


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py2_build

%install
%py2_install

%files -n python2-%{pypi_name}
%{python2_sitelib}/aliyunsdkcore
%{python2_sitelib}/aliyun_python_sdk_core-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.9.5-1
- Initial package.