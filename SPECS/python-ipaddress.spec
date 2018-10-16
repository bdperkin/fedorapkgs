# Created by pyp2rpm-2.0.0
%global pypi_name ipaddress

Name:           python-%{pypi_name}
Version:        1.0.22
Release:        1%{?dist}
Summary:        IPv4/IPv6 manipulation library

License:        Python
URL:            https://github.com/phihag/ipaddress
Source0:        https://files.pythonhosted.org/packages/97/8d/77b8cedcfbf93676148518036c6b1ce7f8e14bf07e95d7fd4ddcb8cc052f/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Port of the 3.3+ ipaddress module to 2.6, 2.7, 3.2

%package -n     python3-%{pypi_name}
Summary:        IPv4/IPv6 manipulation library
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
Port of the 3.3+ ipaddress module to 2.6, 2.7, 3.2


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.md LICENSE
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 1.0.22-1
- Initial package.