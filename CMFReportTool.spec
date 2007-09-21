%define name       CMFReportTool
%define longtitle  A Zope product to generate PDF reports
%define version    0.1.1
%define release    %mkrel 6

Name:               %name
Summary:            %longtitle
Version:            %version
Release:            %release
Group:              Development/Python
Requires:           zope CMF python-reportlab
License:            GPL
URL:                http://www.zope.org/Members/jack-e/CMFReportTool/
BuildRoot:          %{_tmppath}/%{name}-%{version}-rootdir
Buildarch:	    noarch

Source:             http://www.zope.org/Members/jack-e/CMFReportTool/0.1.1/%name-%version.tar.bz2

#----------------------------------------------------------------------
%description
CMFReportTool is a Zope which extends the Zope CMF
to implement PDF skins. PDF skins allow to generate reports
which are automatically converted into PDF files with
the python reportlab library.

#----------------------------------------------------------------------
%prep

rm -rf $RPM_BUILD_ROOT
%setup -q

#----------------------------------------------------------------------
%build

#----------------------------------------------------------------------
%install

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}
install *.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/doc
install doc/*.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/doc
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/doc/examples
install doc/examples/*.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/doc/examples
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/doc/htmldoc
install doc/htmldoc/*.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/doc/htmldoc

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/dtml
install dtml/*.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/dtml

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/help
install help/*.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/help

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/Extensions
install Extensions/*.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/Extensions

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/RenderPDF
install RenderPDF/*.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/RenderPDF

install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins
install -d $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/zpt_reporttool
install skins/zpt_reporttool/*.* $RPM_BUILD_ROOT%{_libdir}/zope/lib/python/Products/%{name}/skins/zpt_reporttool

# correct files.html .css and wrong script encoding
perl -pi -e 's/\015$//' %buildroot/%_libdir/zope/lib/python/Products/CMFReportTool/doc/htmldoc/*.html
perl -pi -e 's/\015$//' %buildroot/%_libdir/zope/lib/python/Products/CMFReportTool/doc/CMFReportTool.odm
perl -pi -e 's/\015$//' %buildroot/%_libdir/zope/lib/python/Products/CMFReportTool/doc/htmldoc/myStylesheet.css

%clean
rm -rf $RPM_BUILD_ROOT

#----------------------------------------------------------------------
%files
%defattr(-,root,root,0755)
%doc README.txt INSTALL.txt TODO.txt LICENSE.txt COPYRIGHT.txt

%{_libdir}/zope/lib/python/Products/%{name}/

#----------------------------------------------------------------------
