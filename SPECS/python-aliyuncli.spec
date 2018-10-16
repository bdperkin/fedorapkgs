# Created by pyp2rpm-3.3.2
%global pypi_name aliyuncli

Name:           python-%{pypi_name}
Version:        2.1.5
Release:        1%{?dist}
Summary:        Universal Command Line Environment for aliyun

License:        None
URL:            http://docs.aliyun.com/?spm=5176.1829009.1002.1.LxlLfS#/pub/aliyun-command-line-interface
Source0:        https://files.pythonhosted.org/packages/source/a/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
BuildRequires:  python2dist(setuptools)
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
Aliyun Command Line Interface Aliyun Command Line Interface aliyuncli is a
unified tool to manage your Aliyun services. Using this tool you can easily
invoke the Aliyun open API to control multiple Aliyun services from the command
line and also automate them through scripts, for instance using the Bash shell
or Python. Aliyuncli on Github - The aliyuncli tool is on Github and anyone can
fork...

%package -n     python2-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python2dist(colorama) <= 0.3.3
Requires:       python2dist(colorama) >= 0.2.5
Requires:       python2dist(jmespath) <= 0.7.1
Requires:       python2dist(jmespath) >= 0.7.0
Requires:       python2dist(setuptools)
%description -n python2-%{pypi_name}
Aliyun Command Line Interface Aliyun Command Line Interface aliyuncli is a
unified tool to manage your Aliyun services. Using this tool you can easily
invoke the Aliyun open API to control multiple Aliyun services from the command
line and also automate them through scripts, for instance using the Bash shell
or Python. Aliyuncli on Github - The aliyuncli tool is on Github and anyone can
fork...

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(colorama) <= 0.3.3
Requires:       python3dist(colorama) >= 0.2.5
Requires:       python3dist(jmespath) <= 0.7.1
Requires:       python3dist(jmespath) >= 0.7.0
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
Aliyun Command Line Interface Aliyun Command Line Interface aliyuncli is a
unified tool to manage your Aliyun services. Using this tool you can easily
invoke the Aliyun open API to control multiple Aliyun services from the command
line and also automate them through scripts, for instance using the Bash shell
or Python. Aliyuncli on Github - The aliyuncli tool is on Github and anyone can
fork...


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
rm -rf %{buildroot}%{_bindir}/*
%py3_install

%files -n python2-%{pypi_name}
%doc README.rst
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python3-%{pypi_name}
%doc README.rst
%{_bindir}/aliyun_completer
%{_bindir}/aliyun_zsh_complete.sh
%{_bindir}/aliyuncli
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.1.5-1
- Initial package.