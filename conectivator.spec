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




%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.2-5mdv2011.0
+ Revision: 617410
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.2-4mdv2010.0
+ Revision: 424939
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.2-3mdv2009.0
+ Revision: 243622
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.2-1mdv2008.1
+ Revision: 136335
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Tue Jun 06 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-06-06 15:35:36 (36723)
- removed %%changelog from spec

* Wed May 31 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-31 14:57:58 (31812)
- released 0.2-1mdk

* Wed May 31 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-31 14:56:21 (31811)
- fix tl alias

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 09:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Fri May 26 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-26 14:15:40 (31618)
- added tms
- ignore errors on unalias

* Fri May 26 2006 Andreas Hasenack <andreas@mandriva.com> 0.1-1mdk
+ 2006-05-26 11:24:10 (31614)
- added svn warning

* Fri May 26 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-26 11:15:55 (31613)
- uploaded files

