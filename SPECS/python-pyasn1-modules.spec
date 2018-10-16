# Created by pyp2rpm-2.0.0
%global pypi_name pyasn1-modules

Name:           python-%{pypi_name}
Version:        0.2.2
Release:        1%{?dist}
Summary:        A collection of ASN.1-based protocols modules

License:        BSD
URL:            https://github.com/etingof/pyasn1-modules
Source0:        https://files.pythonhosted.org/packages/37/33/74ebdc52be534e683dc91faf263931bc00ae05c6073909fde53999088541/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
A collection of ASN.1 modules expressed in form of pyasn1 classes. Includes
protocols PDUs definition (SNMP, LDAP etc.) and various data structures (X.509,
PKCS etc.).

%package -n     python3-%{pypi_name}
Summary:        A collection of ASN.1-based protocols modules
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-pyasn1 >= 0.4.1
Requires:       python3-pyasn1 < 0.5.0
%description -n python3-%{pypi_name}
A collection of ASN.1 modules expressed in form of pyasn1 classes. Includes
protocols PDUs definition (SNMP, LDAP etc.) and various data structures (X.509,
PKCS etc.).


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.md LICENSE.txt
%{python3_sitelib}/pyasn1_modules-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 0.2.2-1
- Initial package.