%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%{!?python_version: %global python_version %(%{__python} -c "from distutils.sysconfig import get_python_version; print get_python_version()")}

Name:           qpid-tests
Version:        0.7.946106
Release:        1%{?dist}
Summary:        Conformance tests for Apache Qpid

Group:          Development/Python
License:        ASL 2.0
URL:            http://qpid.apache.org
Source0:        %{name}-%{version}.tar.gz
# svn export -r<rev> http://svn.apache.org/repos/asf/qpid/trunk/qpid/tests qpid-tests-0.7.<rev>
# tar czf qpid-tests-0.7.<rev>.tar.gz qpid-tests-0.7.<rev>
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

BuildRequires:  python-devel

Requires:       python-qpid >= 0.7
Requires:       python-qmf

%description
Conformance tests for Apache Qpid.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{python_sitelib}/qpid_tests
%doc LICENSE.txt NOTICE.txt

%if "%{python_version}" >= "2.6"
%{python_sitelib}/qpid_tests-*.egg-info
%endif

%changelog
* Wed May 19 2010 Nuno Santos <nsantos@redhat.com> - 0.7.946106-1
- Rebased to svn rev 946106
- Related: rhbz574881

* Mon Apr 19 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.934605-1
- Rebased to svn rev 934605.

* Thu Apr  1 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.930108-1
- Rebased to svn rev 930108.

* Wed Mar  3 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917717-4
- Changed defines to globals and moved them to the top.
- Removed unnecessary python Requires/BuildRequires.

* Tue Mar  2 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917717-3
- Added correct version to python-qpid dependency.

* Mon Mar  1 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917717-2
- Conditionalize egg-info based on python version.

* Mon Mar  1 2010 Rafael Schloming <rafaels@redhat.com> - 0.7.917717-1
- Initial build.
