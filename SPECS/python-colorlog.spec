# Created by pyp2rpm-3.3.2
%global pypi_name colorlog

Name:           python-%{pypi_name}
Version:        3.1.4
Release:        1%{?dist}
Summary:        Log formatting with colors!

License:        MIT License
URL:            https://github.com/borntyping/python-colorlog
Source0:        https://files.pythonhosted.org/packages/source/c/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(colorama)
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(colorama)
BuildRequires:  python3dist(setuptools)

%description
 Log formatting with colors![![]( [![]( [![]( is a formatter for use with
Python's logging module that outputs records using terminal colors.* [Source on
GitHub]( * [Packages on PyPI]( * [Builds on Travis CI](

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(colorama)
%description -n python2-%{pypi_name}
 Log formatting with colors![![]( [![]( [![]( is a formatter for use with
Python's logging module that outputs records using terminal colors.* [Source on
GitHub]( * [Packages on PyPI]( * [Builds on Travis CI](

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(colorama)
%description -n python3-%{pypi_name}
 Log formatting with colors![![]( [![]( [![]( is a formatter for use with
Python's logging module that outputs records using terminal colors.* [Source on
GitHub]( * [Packages on PyPI]( * [Builds on Travis CI](


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
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 3.1.4-1
- Initial package.