# Created by pyp2rpm-2.0.0
%global pypi_name jmespath

Name:           python-%{pypi_name}
Version:        0.9.3
Release:        1%{?dist}
Summary:        JSON Matching Expressions

License:        MIT
URL:            https://github.com/jmespath/jmespath.py
Source0:        https://files.pythonhosted.org/packages/e5/21/795b7549397735e911b032f255cff5fb0de58f96da794274660bca4f58ef/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
JMESPath
========


.. image:: https://badges.gitter.im/Join Chat.svg
:target: https://gitter.im/jmespath/chat


.. image:: https://secure.travis-
ci.org/jmespath/jmespath.py.png?branch=develop
   :target: http://travis-
ci.org/jmespath/jmespath.py


.. image::
https://codecov.io/github/jmespath/jmespath.py/coverage.svg?branch=develop
:target: ...

%package -n     python3-%{pypi_name}
Summary:        JSON Matching Expressions
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
JMESPath
========


.. image:: https://badges.gitter.im/Join Chat.svg
:target: https://gitter.im/jmespath/chat


.. image:: https://secure.travis-
ci.org/jmespath/jmespath.py.png?branch=develop
   :target: http://travis-
ci.org/jmespath/jmespath.py


.. image::
https://codecov.io/github/jmespath/jmespath.py/coverage.svg?branch=develop
:target: ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
cp %{buildroot}/%{_bindir}/jp.py %{buildroot}/%{_bindir}/jp.py-3
ln -sf %{_bindir}/jp.py-3 %{buildroot}/%{_bindir}/jp.py-%{python3_version}


%files -n python3-%{pypi_name} 
%doc README.rst LICENSE.txt
%{_bindir}/jp.py
%{_bindir}/jp.py-3
%{_bindir}/jp.py-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 0.9.3-1
- Initial package.