# Created by pyp2rpm-2.0.0
%global pypi_name aliyuncli

Name:           python-%{pypi_name}
Version:        2.1.5
Release:        1%{?dist}
Summary:        Universal Command Line Environment for aliyun

License:        
URL:            http://docs.aliyun.com/?spm=5176.1829009.1002.1.LxlLfS#/pub/aliyun-command-line-interface
Source0:        https://files.pythonhosted.org/packages/f2/38/a44b5a5d7a33e258113eb88de865c36f14c4d034d17b57ade7dffadab919/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description
Aliyun Command Line Interface
=============================
Overview
------------------
Aliyun Command Line Interface ``aliyuncli`` is a unified
tool to manage your Aliyun services. Using this tool you can easily invoke the
Aliyun open API to control multiple Aliyun services from the command line and
also automate them through scripts, for instance using the Bash shell or
Python. 

Aliyuncli on ...

%package -n     python3-%{pypi_name}
Summary:        Universal Command Line Environment for aliyun
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3-colorama >= 0.2.5
Requires:       python3-colorama <= 0.3.3
Requires:       python3-jmespath >= 0.7.0
Requires:       python3-jmespath <= 0.7.1
Requires:       python3-setuptools
%description -n python3-%{pypi_name}
Aliyun Command Line Interface
=============================
Overview
------------------
Aliyun Command Line Interface ``aliyuncli`` is a unified
tool to manage your Aliyun services. Using this tool you can easily invoke the
Aliyun open API to control multiple Aliyun services from the command line and
also automate them through scripts, for instance using the Bash shell or
Python. 

Aliyuncli on ...

%package -n     python2-%{pypi_name}
Summary:        Universal Command Line Environment for aliyun
%{?python_provide:%python_provide python2-%{pypi_name}}
 
Requires:       python-colorama >= 0.2.5
Requires:       python-colorama <= 0.3.3
Requires:       python-jmespath >= 0.7.0
Requires:       python-jmespath <= 0.7.1
Requires:       python-setuptools
%description -n python2-%{pypi_name}
Aliyun Command Line Interface
=============================
Overview
------------------
Aliyun Command Line Interface ``aliyuncli`` is a unified
tool to manage your Aliyun services. Using this tool you can easily invoke the
Aliyun open API to control multiple Aliyun services from the command line and
also automate them through scripts, for instance using the Bash shell or
Python. 

Aliyuncli on ...


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
cp %{buildroot}/%{_bindir}/aliyun_zsh_complete.sh %{buildroot}/%{_bindir}/aliyun_zsh_complete.sh-2
ln -sf %{_bindir}/aliyun_zsh_complete.sh-2 %{buildroot}/%{_bindir}/aliyun_zsh_complete.sh-%{python2_version}

%py3_install
cp %{buildroot}/%{_bindir}/aliyun_zsh_complete.sh %{buildroot}/%{_bindir}/aliyun_zsh_complete.sh-3
ln -sf %{_bindir}/aliyun_zsh_complete.sh-3 %{buildroot}/%{_bindir}/aliyun_zsh_complete.sh-%{python3_version}


%files -n python3-%{pypi_name} 
%doc README.rst
%{_bindir}/aliyun_zsh_complete.sh
%{_bindir}/aliyun_zsh_complete.sh-3
%{_bindir}/aliyun_zsh_complete.sh-%{python3_version}
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst
%{_bindir}/aliyun_zsh_complete.sh-2
%{_bindir}/aliyun_zsh_complete.sh-%{python2_version}
%{python2_sitelib}/%{pypi_name}
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 2.1.5-1
- Initial package.