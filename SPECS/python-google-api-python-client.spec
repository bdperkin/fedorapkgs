# Created by pyp2rpm-3.3.2
%global pypi_name google-api-python-client

Name:           python-%{pypi_name}
Version:        1.7.4
Release:        1%{?dist}
Summary:        Google API Client Library for Python

License:        Apache 2.0
URL:            http://github.com/google/google-api-python-client/
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(google-auth) >= 1.4.1
BuildRequires:  python2dist(google-auth-httplib2) >= 0.0.3
BuildRequires:  python2dist(httplib2) < 1dev
BuildRequires:  python2dist(httplib2) >= 0.9.2
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2dist(six) < 2dev
BuildRequires:  python2dist(six) >= 1.6.1
BuildRequires:  python2dist(uritemplate) < 4dev
BuildRequires:  python2dist(uritemplate) >= 3.0.0
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(google-auth) >= 1.4.1
BuildRequires:  python3dist(google-auth-httplib2) >= 0.0.3
BuildRequires:  python3dist(httplib2) < 1dev
BuildRequires:  python3dist(httplib2) >= 0.9.2
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) < 2dev
BuildRequires:  python3dist(six) >= 1.6.1
BuildRequires:  python3dist(uritemplate) < 4dev
BuildRequires:  python3dist(uritemplate) >= 3.0.0

%description
The Google API Client for Python is a client library for accessing the Plus,
Moderator, and many other Google APIs.

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(google-auth) >= 1.4.1
Requires:       python2dist(google-auth-httplib2) >= 0.0.3
Requires:       python2dist(httplib2) < 1dev
Requires:       python2dist(httplib2) >= 0.9.2
Requires:       python2dist(six) < 2dev
Requires:       python2dist(six) >= 1.6.1
Requires:       python2dist(uritemplate) < 4dev
Requires:       python2dist(uritemplate) >= 3.0.0
%description -n python2-%{pypi_name}
The Google API Client for Python is a client library for accessing the Plus,
Moderator, and many other Google APIs.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(google-auth) >= 1.4.1
Requires:       python3dist(google-auth-httplib2) >= 0.0.3
Requires:       python3dist(httplib2) < 1dev
Requires:       python3dist(httplib2) >= 0.9.2
Requires:       python3dist(six) < 2dev
Requires:       python3dist(six) >= 1.6.1
Requires:       python3dist(uritemplate) < 4dev
Requires:       python3dist(uritemplate) >= 3.0.0
%description -n python3-%{pypi_name}
The Google API Client for Python is a client library for accessing the Plus,
Moderator, and many other Google APIs.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE
%doc README.md
%{python2_sitelib}/apiclient
%{python2_sitelib}/googleapiclient
%{python2_sitelib}/googleapiclient/discovery_cache
%{python2_sitelib}/google_api_python_client-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/apiclient
%{python3_sitelib}/googleapiclient
%{python3_sitelib}/googleapiclient/discovery_cache
%{python3_sitelib}/google_api_python_client-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 1.7.4-1
- Initial package.