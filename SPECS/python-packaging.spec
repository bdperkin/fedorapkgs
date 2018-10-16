# Created by pyp2rpm-2.0.0
%global pypi_name packaging

Name:           python-%{pypi_name}
Version:        18.0
Release:        1%{?dist}
Summary:        Core utilities for Python packages

License:        ASL %(TODO: version)s and BSD
URL:            https://github.com/pypa/packaging
Source0:        https://files.pythonhosted.org/packages/cf/50/1f10d2626df0aa97ce6b62cf6ebe14f605f4e101234f7748b8da4138a8ed/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

%description
packaging
=========

Core utilities for Python packages


Documentation
-------------

`documentation`_


Discussion
----------

If you run into bugs,
you can file them in our `issue tracker`_.

You can also join ``#pypa`` on
Freenode to ask questions or get involved.


.. _`documentation`:
https://packaging.pypa.io/
.. _`issue tracker`:
https://github.com/pypa/packaging/issues


Code of ...

%package -n     python3-%{pypi_name}
Summary:        Core utilities for Python packages
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-pyparsing >= 2.0.2
Requires:       python3-six
%description -n python3-%{pypi_name}
packaging
=========

Core utilities for Python packages


Documentation
-------------

`documentation`_


Discussion
----------

If you run into bugs,
you can file them in our `issue tracker`_.

You can also join ``#pypa`` on
Freenode to ask questions or get involved.


.. _`documentation`:
https://packaging.pypa.io/
.. _`issue tracker`:
https://github.com/pypa/packaging/issues


Code of ...

%package -n python-%{pypi_name}-doc
Summary:        packaging documentation
%description -n python-%{pypi_name}-doc
Documentation for packaging

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
sphinx-build-3 docs html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst LICENSE LICENSE.APACHE LICENSE.BSD
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 18.0-1
- Initial package.