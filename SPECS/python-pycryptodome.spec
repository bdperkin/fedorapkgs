# Created by pyp2rpm-2.0.0
%global pypi_name pycryptodome

Name:           python-%{pypi_name}
Version:        3.6.6
Release:        1%{?dist}
Summary:        Cryptographic library for Python

License:        BSD and Public Domain
URL:            http://www.pycryptodome.org
Source0:        https://files.pythonhosted.org/packages/94/7f/33b748dd22ea889fcb1a6c6f1f30ad1e5a70066cd7615dbce7d9a6392106/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
PyCryptodome
============

PyCryptodome is a self-contained Python package of
low-level
cryptographic primitives.

It supports Python 2.4 or newer, all
Python 3 versions and PyPy.

You can install it with::

    pip install
pycryptodome

All modules are installed under the ``Crypto`` package.

Check
the pycryptodomex_ project for the equivalent library that
works under the
``Cryptodome`` ...

%package -n     python3-%{pypi_name}
Summary:        Cryptographic library for Python
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}
PyCryptodome
============

PyCryptodome is a self-contained Python package of
low-level
cryptographic primitives.

It supports Python 2.4 or newer, all
Python 3 versions and PyPy.

You can install it with::

    pip install
pycryptodome

All modules are installed under the ``Crypto`` package.

Check
the pycryptodomex_ project for the equivalent library that
works under the
``Cryptodome`` ...

%package -n     python2-%{pypi_name}
Summary:        Cryptographic library for Python
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
PyCryptodome
============

PyCryptodome is a self-contained Python package of
low-level
cryptographic primitives.

It supports Python 2.4 or newer, all
Python 3 versions and PyPy.

You can install it with::

    pip install
pycryptodome

All modules are installed under the ``Crypto`` package.

Check
the pycryptodomex_ project for the equivalent library that
works under the
``Cryptodome`` ...


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


%files -n python3-%{pypi_name} 
%doc README.rst lib/Crypto/SelfTest/Hash/test_vectors/keccak/readme.txt lib/Crypto/SelfTest/Signature/test_vectors/ECDSA/README.txt LICENSE.rst Doc/src/license.rst Doc/LEGAL/copy/LICENSE.orig Doc/LEGAL/copy/LICENSE.python-2.2 Doc/LEGAL/copy/LICENSE.libtom
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst lib/Crypto/SelfTest/Hash/test_vectors/keccak/readme.txt lib/Crypto/SelfTest/Signature/test_vectors/ECDSA/README.txt LICENSE.rst Doc/src/license.rst Doc/LEGAL/copy/LICENSE.orig Doc/LEGAL/copy/LICENSE.python-2.2 Doc/LEGAL/copy/LICENSE.libtom
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 3.6.6-1
- Initial package.