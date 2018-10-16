# Created by pyp2rpm-2.0.0
%global pypi_name httplib2

Name:           python-%{pypi_name}
Version:        0.11.3
Release:        1%{?dist}
Summary:        A comprehensive HTTP client library

License:        MIT
URL:            https://github.com/httplib2/httplib2
Source0:        https://files.pythonhosted.org/packages/fd/ce/aa4a385e3e9fd351737fd2b07edaa56e7a730448465aceda6b35086a0d9b/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A comprehensive HTTP client library, ``httplib2`` supports many features left
out of other HTTP libraries.

**HTTP and HTTPS**
  HTTPS support is only
available if the socket module was compiled with SSL support.


**Keep-Alive**
Supports HTTP 1.1 Keep-Alive, keeping the socket open and performing multiple
requests over the same connection if possible.


**Authentication**
  The
following three ...

%package -n     python3-%{pypi_name}
Summary:        A comprehensive HTTP client library
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
A comprehensive HTTP client library, ``httplib2`` supports many features left
out of other HTTP libraries.

**HTTP and HTTPS**
  HTTPS support is only
available if the socket module was compiled with SSL support.


**Keep-Alive**
Supports HTTP 1.1 Keep-Alive, keeping the socket open and performing multiple
requests over the same connection if possible.


**Authentication**
  The
following three ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 0.11.3-1
- Initial package.