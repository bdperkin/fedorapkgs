# Created by pyp2rpm-2.0.0
%global pypi_name colorlog

Name:           python-%{pypi_name}
Version:        3.1.4
Release:        1%{?dist}
Summary:        Log formatting with colors!

License:        MIT
URL:            https://github.com/borntyping/python-colorlog
Source0:        https://files.pythonhosted.org/packages/2c/a8/8ce4f59cf1fcbb9ebe750fcbab723146d95687c37256ed367a11d9f74265/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description

# Log formatting with colors!

[![](https://img.shields.io/pypi/v/colorlog.svg
)](https://warehouse.python.org/project/colorlog/) [![](https://img.shields.io/
pypi/l/colorlog.svg)](https://warehouse.python.org/project/colorlog/)
[![](https://img.shields.io/travis/borntyping/python-
colorlog/master.svg)](https://travis-ci.org/borntyping/python-colorlog)
`colorlog.ColoredFormatter` is a formatter ...

%package -n     python3-%{pypi_name}
Summary:        Log formatting with colors!
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}

# Log formatting with colors!

[![](https://img.shields.io/pypi/v/colorlog.svg
)](https://warehouse.python.org/project/colorlog/) [![](https://img.shields.io/
pypi/l/colorlog.svg)](https://warehouse.python.org/project/colorlog/)
[![](https://img.shields.io/travis/borntyping/python-
colorlog/master.svg)](https://travis-ci.org/borntyping/python-colorlog)
`colorlog.ColoredFormatter` is a formatter ...

%package -n     python2-%{pypi_name}
Summary:        Log formatting with colors!
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}

# Log formatting with colors!

[![](https://img.shields.io/pypi/v/colorlog.svg
)](https://warehouse.python.org/project/colorlog/) [![](https://img.shields.io/
pypi/l/colorlog.svg)](https://warehouse.python.org/project/colorlog/)
[![](https://img.shields.io/travis/borntyping/python-
colorlog/master.svg)](https://travis-ci.org/borntyping/python-colorlog)
`colorlog.ColoredFormatter` is a formatter ...


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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.md LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 3.1.4-1
- Initial package.