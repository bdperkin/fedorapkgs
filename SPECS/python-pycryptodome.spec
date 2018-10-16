# Created by pyp2rpm-3.3.2
%global pypi_name pycryptodome

Name:           python-%{pypi_name}
Version:        3.6.6
Release:        1%{?dist}
Summary:        Cryptographic library for Python

License:        None
URL:            http://www.pycryptodome.org
Source0:        https://files.pythonhosted.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
PyCryptodome PyCryptodome is a self-contained Python package of low-level
cryptographic primitives.It supports Python 2.4 or newer, all Python 3 versions
and PyPy.You can install it with:: pip install pycryptodomeAll modules are
installed under the Crypto package.Check the pycryptodomex_ project for the
equivalent library that works under the Cryptodome package.PyCryptodome is a
fork of...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
PyCryptodome PyCryptodome is a self-contained Python package of low-level
cryptographic primitives.It supports Python 2.4 or newer, all Python 3 versions
and PyPy.You can install it with:: pip install pycryptodomeAll modules are
installed under the Crypto package.Check the pycryptodomex_ project for the
equivalent library that works under the Cryptodome package.PyCryptodome is a
fork of...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
PyCryptodome PyCryptodome is a self-contained Python package of low-level
cryptographic primitives.It supports Python 2.4 or newer, all Python 3 versions
and PyPy.You can install it with:: pip install pycryptodomeAll modules are
installed under the Crypto package.Check the pycryptodomex_ project for the
equivalent library that works under the Cryptodome package.PyCryptodome is a
fork of...


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py2_build
%py3_build

%install
# Must do the default python version install last because
# the scripts in /usr/bin are overwritten with every setup.py install.
%py2_install
%py3_install

%check
%{__python2} setup.py test
%{__python3} setup.py test

%files -n python2-%{pypi_name}
%license LICENSE.rst Doc/src/license.rst Doc/LEGAL/copy/LICENSE.orig Doc/LEGAL/copy/LICENSE.python-2.2 Doc/LEGAL/copy/LICENSE.libtom
%doc README.rst lib/Crypto/SelfTest/Hash/test_vectors/keccak/readme.txt lib/Crypto/SelfTest/Signature/test_vectors/ECDSA/README.txt
%{python2_sitearch}/Crypto
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%license LICENSE.rst Doc/src/license.rst Doc/LEGAL/copy/LICENSE.orig Doc/LEGAL/copy/LICENSE.python-2.2 Doc/LEGAL/copy/LICENSE.libtom
%doc README.rst lib/Crypto/SelfTest/Hash/test_vectors/keccak/readme.txt lib/Crypto/SelfTest/Signature/test_vectors/ECDSA/README.txt
%{python3_sitearch}/Crypto
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 3.6.6-1
- Initial package.