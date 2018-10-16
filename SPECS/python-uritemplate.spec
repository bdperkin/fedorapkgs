# Created by pyp2rpm-2.0.0
%global pypi_name uritemplate

Name:           python-%{pypi_name}
Version:        3.0.0
Release:        1%{?dist}
Summary:        URI templates

License:        ASL %(TODO: version)s and BSD
URL:            https://uritemplate.readthedocs.org
Source0:        https://files.pythonhosted.org/packages/cd/db/f7b98cdc3f81513fb25d3cbe2501d621882ee81150b745cdd1363278c10a/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

%description
uritemplate
===========

Documentation_ -- GitHub_ -- BitBucket_ -- Travis-CI_
Simple python library to deal with `URI Templates`_. The API looks like

..
code-block:: python

    from uritemplate import URITemplate, expand

    #
NOTE: URI params must be strings not integers

    gist_uri =
'https://api.github.com/users/sigmavirus24/gists{/gist_id}'
    t =
URITemplate(gist_uri)
    ...

%package -n     python3-%{pypi_name}
Summary:        URI templates
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
uritemplate
===========

Documentation_ -- GitHub_ -- BitBucket_ -- Travis-CI_
Simple python library to deal with `URI Templates`_. The API looks like

..
code-block:: python

    from uritemplate import URITemplate, expand

    #
NOTE: URI params must be strings not integers

    gist_uri =
'https://api.github.com/users/sigmavirus24/gists{/gist_id}'
    t =
URITemplate(gist_uri)
    ...

%package -n python-%{pypi_name}-doc
Summary:        uritemplate documentation
%description -n python-%{pypi_name}-doc
Documentation for uritemplate

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
%doc README.rst tests/fixtures/README.md LICENSE LICENSE.APACHE LICENSE.BSD
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 3.0.0-1
- Initial package.