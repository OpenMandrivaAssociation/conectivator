# THIS PACKAGE IS STORED IN SVN
# DON'T UPLOAD WITHOUT FIRST COMMITING YOUR
# CHANGES TO SVN!

Name: conectivator
Summary: A set of aliases for Conectiva users
Version: 0.2
Release: %mkrel 5
License: GPL
Group: Shells
Source0: conectivator-profile.sh
Requires: bash
BuildRoot: %{_tmppath}/%{name}-%{version}-root-%(id -u -n)
Buildarch: noarch

%description
This package provides a set of aliases for users familiar with Conectiva Linux.
Back are:
- l
- tm
- tmm
- tms
- cds

%description -l pt_BR
Este pacote fornece um conjunto de atalhos para usuários familiares com
Conectiva Linux. Entre eles:
- l
- tm
- tmm
- tms
- cds

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 0755 %{_sourcedir}/conectivator-profile.sh \
	%{buildroot}%{_sysconfdir}/profile.d/conectivator.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_sysconfdir}/profile.d/conectivator.sh


