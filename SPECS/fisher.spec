Name:           fisher
Version:        3.2.9
Release:        1%{?dist}
Summary:        A package manager for the fish shell
License:        MIT
BuildArch:      noarch
URL:            https://github.com/jorgebucaran/fisher
Source0:        https://github.com/jorgebucaran/fisher/archive/%{version}.tar.gz
# https://github.com/jorgebucaran/fisher/commit/ae37295f813b07bd7b21c1378e477c6c3f6664d1

BuildRequires:  fish >= 2.2

Requires:       fish >= 2.2
Requires:       curl >= 7.10.3
Requires:       git >= 1.7.12

%description
Fisher is a package manager for the fish shell. It defines a common interface
for package authors to build and distribute shell scripts in a portable way.
You can use it to extend your shell capabilities, change the look of your
prompt and create repeatable configurations across different systems
effortlessly.

%prep
%autosetup

%build

%install
find .. -ls
mkdir -p %{buildroot}%{_sysconfdir}/fish/conf.d
cp -a fisher.fish %{buildroot}%{_sysconfdir}/fish/conf.d/fisher.fish
mkdir -p %{buildroot}%{_pkgdocdir}
cp -a README.md %{buildroot}%{_pkgdocdir}

%clean

%files
%defattr(-,root,root)
%license LICENSE.md
%config(noreplace) %{_sysconfdir}/fish/conf.d/fisher.fish
%{_pkgdocdir}

%changelog
* Wed Oct 16 2019 Brandon Perkins <bperkins@redhat.com> - 3.2.9-1
- Initial package
