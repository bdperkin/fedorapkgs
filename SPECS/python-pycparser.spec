# Created by pyp2rpm-2.0.0
%global pypi_name pycparser

Name:           python-%{pypi_name}
Version:        2.19
Release:        1%{?dist}
Summary:        C parser in Python

License:        BSD
URL:            https://github.com/eliben/pycparser
Source0:        https://files.pythonhosted.org/packages/68/9e/49196946aee219aead1290e00d1e7fdeab8567783e83e1b9ab5585e6206a/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description

        pycparser is a complete parser of the C language, written in
pure Python using the PLY parsing library.
        It parses C code into an AST
and can serve as a front-end for
        C compilers or analysis tools.

%package -n     python3-%{pypi_name}
Summary:        C parser in Python
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python3-%{pypi_name}

        pycparser is a complete parser of the C language, written in
pure Python using the PLY parsing library.
        It parses C code into an AST
and can serve as a front-end for
        C compilers or analysis tools.


%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc README.rst LICENSE
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.19-1
- Initial package.