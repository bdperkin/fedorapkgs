# Created by pyp2rpm-2.0.0
%global pypi_name requestsexceptions

Name:           python-%{pypi_name}
Version:        1.4.0
Release:        1%{?dist}
Summary:        Import exceptions from potentially bundled packages in requests

License:        ASL %(TODO: version)s
URL:            http://www.openstack.org/
Source0:        https://files.pythonhosted.org/packages/82/ed/61b9652d3256503c99b0b8f145d9c8aa24c514caff6efc229989505937c1/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pbr >= 2.0.0
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pbr >= 2.0.0

%description
requestsexceptions
==================

The python requests library bundles the
urllib3 library, however, some
software distributions modify requests to remove
the bundled library.
This makes some operations, such as supressing the
"insecure platform
warning" messages that urllib emits difficult.  This is a
simple
library to find the correct path to exceptions in the requests library
regardless of ...

%package -n     python3-%{pypi_name}
Summary:        Import exceptions from potentially bundled packages in requests
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
requestsexceptions
==================

The python requests library bundles the
urllib3 library, however, some
software distributions modify requests to remove
the bundled library.
This makes some operations, such as supressing the
"insecure platform
warning" messages that urllib emits difficult.  This is a
simple
library to find the correct path to exceptions in the requests library
regardless of ...

%package -n     python2-%{pypi_name}
Summary:        Import exceptions from potentially bundled packages in requests
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
requestsexceptions
==================

The python requests library bundles the
urllib3 library, however, some
software distributions modify requests to remove
the bundled library.
This makes some operations, such as supressing the
"insecure platform
warning" messages that urllib emits difficult.  This is a
simple
library to find the correct path to exceptions in the requests library
regardless of ...


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
%{python3_sitelib}/ 
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst LICENSE
%{python2_sitelib}/ 
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 1.4.0-1
- Initial package.