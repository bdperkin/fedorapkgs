# Created by pyp2rpm-2.0.0
%global pypi_name google-auth-httplib2

Name:           python-%{pypi_name}
Version:        0.0.3
Release:        1%{?dist}
Summary:        Google Authentication Library: httplib2 transport

License:        ASL %(TODO: version)s
URL:            https://github.com/GoogleCloudPlatform/google-auth-library-python-httplib2
Source0:        https://files.pythonhosted.org/packages/e7/32/ac7f30b742276b4911a1439c5291abab1b797ccfd30bc923c5ad67892b13/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
``httplib2`` Transport for Google Auth
======================================
|pypi|

This library provides an `httplib2`_ transport for `google-auth`_.

..
note:: ``httplib`` has lots of problems such as lack of threadsafety
    and
insecure usage of TLS. Using it is highly discouraged. This
    library is
intended to help existing users of ``oauth2client`` migrate to
    ``google-
auth``.

.. ...

%package -n     python3-%{pypi_name}
Summary:        Google Authentication Library: httplib2 transport
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
``httplib2`` Transport for Google Auth
======================================
|pypi|

This library provides an `httplib2`_ transport for `google-auth`_.

..
note:: ``httplib`` has lots of problems such as lack of threadsafety
    and
insecure usage of TLS. Using it is highly discouraged. This
    library is
intended to help existing users of ``oauth2client`` migrate to
    ``google-
auth``.

.. ...

%package -n     python2-%{pypi_name}
Summary:        Google Authentication Library: httplib2 transport
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
``httplib2`` Transport for Google Auth
======================================
|pypi|

This library provides an `httplib2`_ transport for `google-auth`_.

..
note:: ``httplib`` has lots of problems such as lack of threadsafety
    and
insecure usage of TLS. Using it is highly discouraged. This
    library is
intended to help existing users of ``oauth2client`` migrate to
    ``google-
auth``.

.. ...


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
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/google_auth_httplib2.py
%{python3_sitelib}/google_auth_httplib2-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst LICENSE

%{python2_sitelib}/google_auth_httplib2.py*
%{python2_sitelib}/google_auth_httplib2-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 0.0.3-1
- Initial package.