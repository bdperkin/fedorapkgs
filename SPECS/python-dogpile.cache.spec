# Created by pyp2rpm-3.3.2
%global pypi_name dogpile.cache

Name:           python-%{pypi_name}
Version:        0.6.7
Release:        1%{?dist}
Summary:        A caching front-end based on the Dogpile lock

License:        BSD
URL:            http://bitbucket.org/zzzeek/dogpile.cache
Source0:        https://files.pythonhosted.org/packages/source/d/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(mako)
BuildRequires:  python2dist(mock)
BuildRequires:  python2dist(pytest)
BuildRequires:  python2dist(pytest-cov)
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(mako)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-cov)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)

%description
Dogpile consists of two subsystems, one building on top of the other.dogpile
provides the concept of a "dogpile lock", a control structure which allows a
single thread of execution to be selected as the "creator" of some resource,
while allowing other threads of execution to refer to the previous version of
this resource as the creation proceeds; if there is no previous version, then
those...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Dogpile consists of two subsystems, one building on top of the other.dogpile
provides the concept of a "dogpile lock", a control structure which allows a
single thread of execution to be selected as the "creator" of some resource,
while allowing other threads of execution to refer to the previous version of
this resource as the creation proceeds; if there is no previous version, then
those...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Dogpile consists of two subsystems, one building on top of the other.dogpile
provides the concept of a "dogpile lock", a control structure which allows a
single thread of execution to be selected as the "creator" of some resource,
while allowing other threads of execution to refer to the previous version of
this resource as the creation proceeds; if there is no previous version, then
those...

%package -n python-%{pypi_name}-doc
Summary:        dogpile.cache documentation
%description -n python-%{pypi_name}-doc
Documentation for dogpile.cache

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build
# generate html docs 
PYTHONPATH=${PWD} sphinx-build-3 docs/build html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

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
%doc README.rst docs/build/unreleased/README.txt
%{python2_sitelib}/dogpile
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst docs/build/unreleased/README.txt
%{python3_sitelib}/dogpile
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html
%license LICENSE

%changelog
* Tue Oct 16 2018 root - 0.6.7-1
- Initial package.