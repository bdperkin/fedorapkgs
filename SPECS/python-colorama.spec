# Created by pyp2rpm-2.0.0
%global pypi_name colorama

Name:           python-%{pypi_name}
Version:        0.4.0
Release:        1%{?dist}
Summary:        Cross-platform colored terminal text

License:        BSD
URL:            https://github.com/tartley/colorama
Source0:        https://files.pythonhosted.org/packages/0a/93/6e8289231675d561d476d656c2ee3a868c1cca207e16c118d4503b25e2bf/%{pypi_name}-%{version}-py2.py3-none-any.whl
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
.. image:: https://img.shields.io/pypi/v/colorama.svg
    :target:
https://pypi.org/project/colorama/
    :alt: Latest Version

.. image::
https://img.shields.io/pypi/pyversions/colorama.svg
    :target:
https://pypi.org/project/colorama/
    :alt: Supported Python versions

..
image:: https://travis-ci.org/tartley/colorama.svg?branch=master
    :target:
https://travis-ci.org/tartley/colorama
    ...

%package -n     python3-%{pypi_name}
Summary:        Cross-platform colored terminal text
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
.. image:: https://img.shields.io/pypi/v/colorama.svg
    :target:
https://pypi.org/project/colorama/
    :alt: Latest Version

.. image::
https://img.shields.io/pypi/pyversions/colorama.svg
    :target:
https://pypi.org/project/colorama/
    :alt: Supported Python versions

..
image:: https://travis-ci.org/tartley/colorama.svg?branch=master
    :target:
https://travis-ci.org/tartley/colorama
    ...

%package -n     python2-%{pypi_name}
Summary:        Cross-platform colored terminal text
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
.. image:: https://img.shields.io/pypi/v/colorama.svg
    :target:
https://pypi.org/project/colorama/
    :alt: Latest Version

.. image::
https://img.shields.io/pypi/pyversions/colorama.svg
    :target:
https://pypi.org/project/colorama/
    :alt: Supported Python versions

..
image:: https://travis-ci.org/tartley/colorama.svg?branch=master
    :target:
https://travis-ci.org/tartley/colorama
    ...


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
%py2_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%py3_install


%files -n python3-%{pypi_name} 
%doc LICENSE.txt
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc LICENSE.txt
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 0.4.0-1
- Initial package.