# Created by pyp2rpm-2.0.0
%global pypi_name asn1crypto

Name:           python-%{pypi_name}
Version:        0.24.0
Release:        1%{?dist}
Summary:        Fast ASN.1 parser and serializer with definitions for private keys, public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509 and TSP

License:        MIT
URL:            https://github.com/wbond/asn1crypto
Source0:        https://files.pythonhosted.org/packages/fc/f1/8db7daa71f414ddabfa056c4ef792e1461ff655c2ae2928a2b675bfed6b4/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
Docs for this project are maintained at
https://github.com/wbond/asn1crypto#readme.

%package -n     python3-%{pypi_name}
Summary:        Fast ASN.1 parser and serializer with definitions for private keys, public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509 and TSP
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
Docs for this project are maintained at
https://github.com/wbond/asn1crypto#readme.

%package -n     python2-%{pypi_name}
Summary:        Fast ASN.1 parser and serializer with definitions for private keys, public keys, certificates, CRL, OCSP, CMS, PKCS#3, PKCS#7, PKCS#8, PKCS#12, PKCS#5, X.509 and TSP
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
Docs for this project are maintained at
https://github.com/wbond/asn1crypto#readme.


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
%doc docs/readme.md readme.md LICENSE
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc docs/readme.md readme.md LICENSE
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 0.24.0-1
- Initial package.