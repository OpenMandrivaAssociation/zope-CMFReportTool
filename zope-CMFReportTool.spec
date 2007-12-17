%define Product CMFReportTool
%define product cmfreporttool
%define name    zope-%{Product}
%define version 0.1.1
%define release %mkrel 7

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
Buildarch:  noarch

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
