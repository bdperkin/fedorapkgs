# Created by pyp2rpm-2.0.0
%global pypi_name cachetools

Name:           python-%{pypi_name}
Version:        2.1.0
Release:        1%{?dist}
Summary:        Extensible memoizing collections and decorators

License:        MIT
URL:            https://github.com/tkem/cachetools
Source0:        https://files.pythonhosted.org/packages/87/41/b3e00059f3c34b57a653d2120d213715abb4327b36fee22e59c1da977d25/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
BuildRequires:  python-sphinx

%description
cachetools
========================================================================

This
module provides various memoizing collections and decorators,
including
variants of the Python 3 Standard Library `@lru_cache`_
function decorator.

..
code-block:: pycon

   >>> from cachetools import LRUCache
   >>> cache =
LRUCache(maxsize=2)
   >>> cache.update([('first', 1), ('second', 2)])
   >>>
...

%package -n     python3-%{pypi_name}
Summary:        Extensible memoizing collections and decorators
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
cachetools
========================================================================

This
module provides various memoizing collections and decorators,
including
variants of the Python 3 Standard Library `@lru_cache`_
function decorator.

..
code-block:: pycon

   >>> from cachetools import LRUCache
   >>> cache =
LRUCache(maxsize=2)
   >>> cache.update([('first', 1), ('second', 2)])
   >>>
...

%package -n     python2-%{pypi_name}
Summary:        Extensible memoizing collections and decorators
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
cachetools
========================================================================

This
module provides various memoizing collections and decorators,
including
variants of the Python 3 Standard Library `@lru_cache`_
function decorator.

..
code-block:: pycon

   >>> from cachetools import LRUCache
   >>> cache =
LRUCache(maxsize=2)
   >>> cache.update([('first', 1), ('second', 2)])
   >>>
...

%package -n python-%{pypi_name}-doc
Summary:        cachetools documentation
%description -n python-%{pypi_name}-doc
Documentation for cachetools

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
%py2_build
# generate html docs 
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 2.1.0-1
- Initial package.