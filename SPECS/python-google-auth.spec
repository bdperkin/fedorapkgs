# Created by pyp2rpm-3.3.2
%global pypi_name google-auth

Name:           python-%{pypi_name}
Version:        1.5.1
Release:        1%{?dist}
Summary:        Google Authentication Library

License:        Apache 2.0
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python
Source0:        https://files.pythonhosted.org/packages/source/g/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(cachetools) >= 2.0.0
BuildRequires:  python2dist(pyasn1-modules) >= 0.2.1
BuildRequires:  python2dist(rsa) >= 3.1.4
BuildRequires:  python2dist(setuptools)
BuildRequires:  python2dist(six) >= 1.9.0
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(cachetools) >= 2.0.0
BuildRequires:  python3dist(pyasn1-modules) >= 0.2.1
BuildRequires:  python3dist(rsa) >= 3.1.4
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six) >= 1.9.0

%description
Google Auth Python Library |build| |docs| |pypi|This library simplifies using
Google's various server-to-server authentication mechanisms to access Google
APIs... |buil .. |doc .. |pyp Installing

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(cachetools) >= 2.0.0
Requires:       python2dist(pyasn1-modules) >= 0.2.1
Requires:       python2dist(rsa) >= 3.1.4
Requires:       python2dist(six) >= 1.9.0
%description -n python2-%{pypi_name}
Google Auth Python Library |build| |docs| |pypi|This library simplifies using
Google's various server-to-server authentication mechanisms to access Google
APIs... |buil .. |doc .. |pyp Installing

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(cachetools) >= 2.0.0
Requires:       python3dist(pyasn1-modules) >= 0.2.1
Requires:       python3dist(rsa) >= 3.1.4
Requires:       python3dist(six) >= 1.9.0
%description -n python3-%{pypi_name}
Google Auth Python Library |build| |docs| |pypi|This library simplifies using
Google's various server-to-server authentication mechanisms to access Google
APIs... |buil .. |doc .. |pyp Installing


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
%doc README.rst
%{python2_sitelib}/google
%{python2_sitelib}/google_auth-%{version}-py?.?-*.pth
%{python2_sitelib}/google_auth-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/google
%{python3_sitelib}/google_auth-%{version}-py?.?-*.pth
%{python3_sitelib}/google_auth-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 1.5.1-1
- Initial package.