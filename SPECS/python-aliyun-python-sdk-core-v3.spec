# Created by pyp2rpm-3.3.2
%global pypi_name aliyun-python-sdk-core-v3

Name:           python-%{pypi_name}
Version:        2.9.4
Release:        1%{?dist}
Summary:        The core module of Aliyun Python3 SDK

License:        Apache
URL:            http://develop.aliyun.com/sdk/python
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
 aliyun-python-sdk-core This is the core module of Aliyun Python SDK.Aliyun
Python SDK is the official software development kit. It makes things easy to
integrate your Python application, library, or script with Aliyun services.This
module works on Python versions: * 3.0.0 and greater Documentation:Please visit

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(pycryptodome) >= 3.4.7
%description -n python3-%{pypi_name}
 aliyun-python-sdk-core This is the core module of Aliyun Python SDK.Aliyun
Python SDK is the official software development kit. It makes things easy to
integrate your Python application, library, or script with Aliyun services.This
module works on Python versions: * 3.0.0 and greater Documentation:Please visit


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst
%{python3_sitelib}/aliyunsdkcore
%{python3_sitelib}/aliyun_python_sdk_core_v3-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.9.4-1
- Initial package.