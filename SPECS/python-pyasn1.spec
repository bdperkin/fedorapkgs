# Created by pyp2rpm-2.0.0
%global pypi_name pyasn1

Name:           python-%{pypi_name}
Version:        0.4.4
Release:        1%{?dist}
Summary:        ASN.1 types and codecs

License:        BSD
URL:            https://github.com/etingof/pyasn1
Source0:        https://files.pythonhosted.org/packages/10/46/059775dc8e50f722d205452bced4b3cc965d27e8c3389156acd3b1123ae3/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx

%description
Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)

%package -n     python3-%{pypi_name}
Summary:        ASN.1 types and codecs
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Pure-Python implementation of ASN.1 types and DER/BER/CER codecs (X.208)

%package -n python-%{pypi_name}-doc
Summary:        pyasn1 documentation
%description -n python-%{pypi_name}-doc
Documentation for pyasn1

%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build
# generate html docs 
sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.md docs/source/license.rst LICENSE.rst
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python-%{pypi_name}-doc
%doc html 

%changelog
* Tue Oct 16 2018 root - 0.4.4-1
- Initial package.