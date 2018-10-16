# Created by pyp2rpm-2.0.0
%global pypi_name pyparsing

Name:           python-%{pypi_name}
Version:        2.2.2
Release:        1%{?dist}
Summary:        Python parsing module

License:        MIT
URL:            https://github.com/pyparsing/pyparsing/
Source0:        https://files.pythonhosted.org/packages/1a/e2/4a7ad8f2808e03caebd3ec0a250b4afbb26d4ba063c39c3286185dd06dd1/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description


%package -n     python3-%{pypi_name}
Summary:        Python parsing module
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}



%prep
%autosetup -n %{pypi_name}-%{version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install


%files -n python3-%{pypi_name} 
%doc examples/0README.html README.md LICENSE
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.2.2-1
- Initial package.