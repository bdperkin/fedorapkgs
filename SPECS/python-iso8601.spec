# Created by pyp2rpm-2.0.0
%global pypi_name iso8601

Name:           python-%{pypi_name}
Version:        0.1.12
Release:        1%{?dist}
Summary:        Simple module to parse ISO 8601 dates

License:        MIT
URL:            https://bitbucket.org/micktwomey/pyiso8601
Source0:        https://files.pythonhosted.org/packages/45/13/3db24895497345fb44c4248c08b16da34a9eb02643cea2754b21b5ed08b0/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Simple module to parse ISO 8601 dates

This module parses the most common forms
of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime
objects.

>>> import iso8601
>>> iso8601.parse_date("2007-01-25T12:00:00Z")
datetime.datetime(2007, 1, 25, 12, 0, tzinfo=<iso8601.Utc>)
>>>

See the
LICENSE file for the license this package is released under.

If you want more
full featured ...

%package -n     python3-%{pypi_name}
Summary:        Simple module to parse ISO 8601 dates
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Simple module to parse ISO 8601 dates

This module parses the most common forms
of ISO 8601 date strings (e.g.
2007-01-14T20:34:22+00:00) into datetime
objects.

>>> import iso8601
>>> iso8601.parse_date("2007-01-25T12:00:00Z")
datetime.datetime(2007, 1, 25, 12, 0, tzinfo=<iso8601.Utc>)
>>>

See the
LICENSE file for the license this package is released under.

If you want more
full featured ...


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
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Tue Oct 16 2018 root - 0.1.12-1
- Initial package.