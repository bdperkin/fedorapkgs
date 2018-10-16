# Created by pyp2rpm-2.0.0
%global pypi_name appdirs

Name:           python-%{pypi_name}
Version:        1.4.3
Release:        1%{?dist}
Summary:        A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir"

License:        MIT
URL:            http://github.com/ActiveState/appdirs
Source0:        https://files.pythonhosted.org/packages/48/69/d87c60746b393309ca30761f8e2b49473d43450b150cb08f3c6df5c11be5/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
 
BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%description

.. image:: https://secure.travis-ci.org/ActiveState/appdirs.png
    :target:
http://travis-ci.org/ActiveState/appdirs

the problem
===========

What
directory should your app use for storing user data? If running on Mac OS X,
you
should use::

    ~/Library/Application Support/<AppName>

If on Windows
(at least English Win XP) that should be::

    C:\Documents and
Settings\<User>\Application ...

%package -n     python3-%{pypi_name}
Summary:        A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir"
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}

.. image:: https://secure.travis-ci.org/ActiveState/appdirs.png
    :target:
http://travis-ci.org/ActiveState/appdirs

the problem
===========

What
directory should your app use for storing user data? If running on Mac OS X,
you
should use::

    ~/Library/Application Support/<AppName>

If on Windows
(at least English Win XP) that should be::

    C:\Documents and
Settings\<User>\Application ...

%package -n     python2-%{pypi_name}
Summary:        A small Python module for determining appropriate platform-specific dirs, e.g. a "user data dir"
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}

.. image:: https://secure.travis-ci.org/ActiveState/appdirs.png
    :target:
http://travis-ci.org/ActiveState/appdirs

the problem
===========

What
directory should your app use for storing user data? If running on Mac OS X,
you
should use::

    ~/Library/Application Support/<AppName>

If on Windows
(at least English Win XP) that should be::

    C:\Documents and
Settings\<User>\Application ...


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


%check
%{__python3} setup.py test
%{__python2} setup.py test

%files -n python3-%{pypi_name} 
%doc README.rst LICENSE.txt
%dir %{python3_sitelib}/__pycache__/
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/%{pypi_name}.py
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%files -n python2-%{pypi_name} 
%doc README.rst LICENSE.txt

%{python2_sitelib}/%{pypi_name}.py*
%{python2_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 1.4.3-1
- Initial package.