# Created by pyp2rpm-3.3.2
%global pypi_name PyYAML

Name:           python-%{pypi_name}
Version:        3.13
Release:        1%{?dist}
Summary:        YAML parser and emitter for Python

License:        MIT
URL:            http://pyyaml.org/wiki/PyYAML
Source0:        https://files.pythonhosted.org/packages/source/P/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages. PyYAML is a YAML parser and emitter for
Python.PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages. PyYAML supports
standard YAML tags and provides Python-specific tags that allow to represent an
arbitrary...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
YAML is a data serialization format designed for human readability and
interaction with scripting languages. PyYAML is a YAML parser and emitter for
Python.PyYAML features a complete YAML 1.1 parser, Unicode support, pickle
support, capable extension API, and sensible error messages. PyYAML supports
standard YAML tags and provides Python-specific tags that allow to represent an
arbitrary...


%prep
%autosetup -n %{pypi_name}-%{version}

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%license LICENSE
%{python3_sitearch}/yaml
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 3.13-1
- Initial package.