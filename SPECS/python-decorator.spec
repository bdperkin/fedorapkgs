# Created by pyp2rpm-2.0.0
%global pypi_name decorator

Name:           python-%{pypi_name}
Version:        4.3.0
Release:        1%{?dist}
Summary:        Better living through Python with decorators

License:        BSD
URL:            https://github.com/micheles/decorator
Source0:        https://files.pythonhosted.org/packages/6f/24/15a229626c775aae5806312f6bf1e2a73785be3402c0acdec5dbddd8c11e/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
Decorator module
=================

:Author: Michele Simionato
:E-mail:
michele.simionato@gmail.com
:Requires: Python from 2.6 to 3.6
:Download page:
http://pypi.python.org/pypi/decorator
:Installation: ``pip install decorator``
:License: BSD license

Installation
-------------

If you are lazy, just
perform

 `$ pip install decorator`

which will install just the module on your
system.

If you ...

%package -n     python3-%{pypi_name}
Summary:        Better living through Python with decorators
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Decorator module
=================

:Author: Michele Simionato
:E-mail:
michele.simionato@gmail.com
:Requires: Python from 2.6 to 3.6
:Download page:
http://pypi.python.org/pypi/decorator
:Installation: ``pip install decorator``
:License: BSD license

Installation
-------------

If you are lazy, just
perform

 `$ pip install decorator`

which will install just the module on your
system.

If you ...

%package -n     python2-%{pypi_name}
Summary:        Better living through Python with decorators
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Decorator module
=================

:Author: Michele Simionato
:E-mail:
michele.simionato@gmail.com
:Requires: Python from 2.6 to 3.6
:Download page:
http://pypi.python.org/pypi/decorator
:Installation: ``pip install decorator``
:License: BSD license

Installation
-------------

If you are lazy, just
perform

 `$ pip install decorator`

which will install just the module on your
system.

If you ...


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


%check
%{__python3} setup.py test
%{__python2} setup.py test

%files -n python3-%{pypi_name} 
%doc README.md docs/README.rst LICENSE.txt
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.md docs/README.rst LICENSE.txt

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 4.3.0-1
- Initial package.