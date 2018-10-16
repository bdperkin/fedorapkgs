# Created by pyp2rpm-2.0.0
%global pypi_name google-api-python-client

Name:           python-%{pypi_name}
Version:        1.7.4
Release:        1%{?dist}
Summary:        Google API Client Library for Python

License:        ASL %(TODO: version)s
URL:            http://github.com/google/google-api-python-client/
Source0:        https://files.pythonhosted.org/packages/4e/92/e4746e646585c8c359781c19984fe8b6b8794a6cfe382cd481329d5252ac/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
The Google API Client for Python is a client library for
accessing the Plus,
Moderator, and many other Google APIs.

%package -n     python3-%{pypi_name}
Summary:        Google API Client Library for Python
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
 
Requires:       python3-httplib2 >= 0.9.2
Requires:       python3-httplib2 < 1dev
Requires:       python3-google-auth >= 1.4.1
Requires:       python3-google-auth-httplib2 >= 0.0.3
Requires:       python3-six >= 1.6.1
Requires:       python3-six < 2dev
Requires:       python3-uritemplate >= 3.0.0
Requires:       python3-uritemplate < 4dev
%description -n python3-%{pypi_name}
The Google API Client for Python is a client library for
accessing the Plus,
Moderator, and many other Google APIs.

%package -n     python2-%{pypi_name}
Summary:        Google API Client Library for Python
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-httplib2 >= 0.9.2
Requires:       python-httplib2 < 1dev
Requires:       python-google-auth >= 1.4.1
Requires:       python-google-auth-httplib2 >= 0.0.3
Requires:       python-six >= 1.6.1
Requires:       python-six < 2dev
Requires:       python-uritemplate >= 3.0.0
Requires:       python-uritemplate < 4dev
%description -n python2-%{pypi_name}
The Google API Client for Python is a client library for
accessing the Plus,
Moderator, and many other Google APIs.


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
%doc README.md LICENSE
%{python3_sitelib}/apiclient
%{python3_sitelib}/googleapiclient
%{python3_sitelib}/googleapiclient/discovery_cache
%{python3_sitelib}/google_api_python_client-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.md LICENSE
%{python2_sitelib}/apiclient
%{python2_sitelib}/googleapiclient
%{python2_sitelib}/googleapiclient/discovery_cache
%{python2_sitelib}/google_api_python_client-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 1.7.4-1
- Initial package.