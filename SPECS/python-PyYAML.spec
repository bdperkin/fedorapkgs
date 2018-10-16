# Created by pyp2rpm-2.0.0
%global pypi_name PyYAML

Name:           python-%{pypi_name}
Version:        3.13
Release:        1%{?dist}
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            http://pyyaml.org/wiki/PyYAML
Source0:        https://files.pythonhosted.org/packages/9e/a3/1d13970c3f36777c583f136c136f804d70f500168edc1edea6daa7200769/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
YAML is a data serialization format designed for human readability
and
interaction with scripting languages.  PyYAML is a YAML parser
and emitter for
Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports
standard YAML tags and provides Python-specific tags that
allow to represent an
arbitrary ...

%package -n     python3-%{pypi_name}
Summary:        YAML parser and emitter for Python
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
YAML is a data serialization format designed for human readability
and
interaction with scripting languages.  PyYAML is a YAML parser
and emitter for
Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports
standard YAML tags and provides Python-specific tags that
allow to represent an
arbitrary ...

%package -n     python2-%{pypi_name}
Summary:        YAML parser and emitter for Python
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
YAML is a data serialization format designed for human readability
and
interaction with scripting languages.  PyYAML is a YAML parser
and emitter for
Python.

PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages.  PyYAML
supports
standard YAML tags and provides Python-specific tags that
allow to represent an
arbitrary ...


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build
%py2_build

%install
# Must do the subpackages' install first because the scripts in /usr/bin are
# overwritten with every setup.py install.
%py2_install

%py3_install


%files -n python3-%{pypi_name} 
%doc LICENSE
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc LICENSE
%{python2_sitearch}/%{pypi_name}
%{python2_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 3.13-1
- Initial package.