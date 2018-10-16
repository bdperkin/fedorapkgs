# Created by pyp2rpm-2.0.0
%global pypi_name munch

Name:           python-%{pypi_name}
Version:        2.3.2
Release:        1%{?dist}
Summary:        A dot-accessible dictionary (a la JavaScript objects)

License:        MIT
URL:            http://github.com/Infinidat/munch
Source0:        https://files.pythonhosted.org/packages/68/f4/260ec98ea840757a0da09e0ed8135333d59b8dfebe9752a365b04857660a/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description


%package -n     python3-%{pypi_name}
Summary:        A dot-accessible dictionary (a la JavaScript objects)
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}
 
Requires:       python3-six
%description -n python3-%{pypi_name}


%package -n     python2-%{pypi_name}
Summary:        A dot-accessible dictionary (a la JavaScript objects)
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-six
%description -n python2-%{pypi_name}



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
%doc README.md LICENSE.txt
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.md LICENSE.txt
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.3.2-1
- Initial package.