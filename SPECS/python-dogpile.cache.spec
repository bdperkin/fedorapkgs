# Created by pyp2rpm-2.0.0
%global pypi_name dogpile.cache

Name:           python-%{pypi_name}
Version:        0.6.7
Release:        1%{?dist}
Summary:        A caching front-end based on the Dogpile lock

License:        BSD
URL:            http://bitbucket.org/zzzeek/dogpile.cache
Source0:        https://files.pythonhosted.org/packages/ee/bd/440da735a11c6087eed7cc8747fc4b995cbac2464168682f8ee1c8e43844/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-pytest-cov
BuildRequires:  python3-mock
BuildRequires:  python3-Mako
BuildRequires:  python3-sphinx
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-pytest
BuildRequires:  python-pytest-cov
BuildRequires:  python-mock
BuildRequires:  python-Mako
BuildRequires:  python-sphinx

%description
dogpile
=======

Dogpile consists of two subsystems, one building on top of the
other.

``dogpile`` provides the concept of a "dogpile lock", a control
structure
which allows a single thread of execution to be selected as the
"creator" of
some resource, while allowing other threads of execution to refer
to the previous
version of this resource as the creation proceeds; if there is
no ...

%package -n     python3-%{pypi_name}
Summary:        A caching front-end based on the Dogpile lock
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
 
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
dogpile
=======

Dogpile consists of two subsystems, one building on top of the
other.

``dogpile`` provides the concept of a "dogpile lock", a control
structure
which allows a single thread of execution to be selected as the
"creator" of
some resource, while allowing other threads of execution to refer
to the previous
version of this resource as the creation proceeds; if there is
no ...

%package -n     python2-%{pypi_name}
Summary:        A caching front-end based on the Dogpile lock
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-setuptools
%description -n python2-%{pypi_name}
dogpile
=======

Dogpile consists of two subsystems, one building on top of the
other.

``dogpile`` provides the concept of a "dogpile lock", a control
structure
which allows a single thread of execution to be selected as the
"creator" of
some resource, while allowing other threads of execution to refer
to the previous
version of this resource as the creation proceeds; if there is
no ...

%package -n python-%{pypi_name}-doc
Summary:        dogpile.cache documentation
%description -n python-%{pypi_name}-doc
Documentation for dogpile.cache

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%py2_build
# generate html docs 
sphinx-build-3 docs/build html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst docs/build/unreleased/README.txt LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?-*.pth
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst docs/build/unreleased/README.txt LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?-*.pth
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 0.6.7-1
- Initial package.