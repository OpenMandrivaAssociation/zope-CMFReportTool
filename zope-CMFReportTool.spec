%define Product CMFReportTool
%define product cmfreporttool
%define name    zope-%{Product}
%define version 0.1.1
%define release %mkrel 11

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:    A Zope product to generate PDF reports
Group:      Development/Python
License:    GPL
Group:      System/Servers
URL:        http://www.zope.org/Members/jack-e/CMFReportTool/
Source:     http://www.zope.org/Members/jack-e/CMFReportTool/%{version}/%{Product}-%{version}.tar.bz2
Requires:   zope
Obsoletes:  %{Product}
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
CMFReportTool is a Zope which extends the Zope CMF
to implement PDF skins. PDF skins allow to generate reports
which are automatically converted into PDF files with
the python reportlab library.

%prep
%setup -q -n %{Product}-%{version}

%build

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_libdir}/zope/lib/python/Products/%{Product}
cp -pr * %{buildroot}%{_libdir}/zope/lib/python/Products/%{Product}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README.txt INSTALL.txt TODO.txt LICENSE.txt COPYRIGHT.txt
%{_libdir}/zope/lib/python/Products/%{Product}


%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-11mdv2010.0
+ Revision: 435529
- rebuild
- rebuild

* Sat Aug 09 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1.1-9mdv2009.0
+ Revision: 269878
- rebuild early 2009.0 package (before pixel changes)

* Sun May 11 2008 Nicolas Lécureuil <neoclust@mandriva.org> 0.1.1-8mdv2009.0
+ Revision: 205680
- Should not be noarch ed

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.1-7mdv2008.0
+ Revision: 91820
- spec cleanup
  package renaming
- package renaming
- import CMFReportTool

