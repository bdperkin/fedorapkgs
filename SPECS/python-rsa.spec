# Created by pyp2rpm-2.0.0
%global pypi_name rsa

Name:           python-%{pypi_name}
Version:        4.0
Release:        1%{?dist}
Summary:        Pure-Python RSA implementation

License:        Apache 2.0
URL:            https://stuvel.eu/rsa
Source0:        https://files.pythonhosted.org/packages/cb/d0/8f99b91432a60ca4b1cd478fd0bdf28c1901c58e3a9f14f4ba3dba86b57f/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Pure Python RSA implementation
==============================
[![PyPI](https://img.shields.io/pypi/v/rsa.svg)](https://pypi.org/project/rsa/)
[![Build Status](https://travis-ci.org/sybrenstuvel/python-
rsa.svg?branch=master)](https://travis-ci.org/sybrenstuvel/python-rsa)
[![Coverage ...

%package -n     python3-%{pypi_name}
Summary:        Pure-Python RSA implementation
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
 
Requires:       python3-pyasn1 >= 0.1.3
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
Pure Python RSA implementation
==============================
[![PyPI](https://img.shields.io/pypi/v/rsa.svg)](https://pypi.org/project/rsa/)
[![Build Status](https://travis-ci.org/sybrenstuvel/python-
rsa.svg?branch=master)](https://travis-ci.org/sybrenstuvel/python-rsa)
[![Coverage ...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install
cp %{buildroot}/%{_bindir}/pyrsa-priv2pub %{buildroot}/%{_bindir}/pyrsa-priv2pub-3
ln -sf %{_bindir}/pyrsa-priv2pub-3 %{buildroot}/%{_bindir}/pyrsa-priv2pub-%{python3_version}
cp %{buildroot}/%{_bindir}/pyrsa-keygen %{buildroot}/%{_bindir}/pyrsa-keygen-3
ln -sf %{_bindir}/pyrsa-keygen-3 %{buildroot}/%{_bindir}/pyrsa-keygen-%{python3_version}
cp %{buildroot}/%{_bindir}/pyrsa-encrypt %{buildroot}/%{_bindir}/pyrsa-encrypt-3
ln -sf %{_bindir}/pyrsa-encrypt-3 %{buildroot}/%{_bindir}/pyrsa-encrypt-%{python3_version}
cp %{buildroot}/%{_bindir}/pyrsa-decrypt %{buildroot}/%{_bindir}/pyrsa-decrypt-3
ln -sf %{_bindir}/pyrsa-decrypt-3 %{buildroot}/%{_bindir}/pyrsa-decrypt-%{python3_version}
cp %{buildroot}/%{_bindir}/pyrsa-sign %{buildroot}/%{_bindir}/pyrsa-sign-3
ln -sf %{_bindir}/pyrsa-sign-3 %{buildroot}/%{_bindir}/pyrsa-sign-%{python3_version}
cp %{buildroot}/%{_bindir}/pyrsa-verify %{buildroot}/%{_bindir}/pyrsa-verify-3
ln -sf %{_bindir}/pyrsa-verify-3 %{buildroot}/%{_bindir}/pyrsa-verify-%{python3_version}


%files -n python3-%{pypi_name} 
%doc README.md LICENSE
%{_bindir}/pyrsa-priv2pub
%{_bindir}/pyrsa-priv2pub-3
%{_bindir}/pyrsa-priv2pub-%{python3_version}
%{_bindir}/pyrsa-keygen
%{_bindir}/pyrsa-keygen-3
%{_bindir}/pyrsa-keygen-%{python3_version}
%{_bindir}/pyrsa-encrypt
%{_bindir}/pyrsa-encrypt-3
%{_bindir}/pyrsa-encrypt-%{python3_version}
%{_bindir}/pyrsa-decrypt
%{_bindir}/pyrsa-decrypt-3
%{_bindir}/pyrsa-decrypt-%{python3_version}
%{_bindir}/pyrsa-sign
%{_bindir}/pyrsa-sign-3
%{_bindir}/pyrsa-sign-%{python3_version}
%{_bindir}/pyrsa-verify
%{_bindir}/pyrsa-verify-3
%{_bindir}/pyrsa-verify-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 4.0-1
- Initial package.