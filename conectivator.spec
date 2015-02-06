Summary:	A set of aliases for Conectiva users
Name:		conectivator
Version:	0.2
Release:	7
License:	GPLv2+
Group:		Shells
Source0:	conectivator-profile.sh
Requires:	bash
Buildarch:	noarch

%files
%{_sysconfdir}/profile.d/conectivator.sh

#----------------------------------------------------------------------------

%description
This package provides a set of aliases for users familiar with Conectiva Linux.
Back are:
- l
- tm
- tmm
- tms
- cds

%install
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 0755 %{SOURCE0} %{buildroot}%{_sysconfdir}/profile.d/conectivator.sh

