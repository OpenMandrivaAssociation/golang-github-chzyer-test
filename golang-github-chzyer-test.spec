# Run tests in check section
%bcond_without check

%global goipath         github.com/chzyer/test
%global commit          a1ea475d72b168a29f44221e0ad031a842642302

%global common_description %{expand:
Golang test utility.}

%gometa

Name:    %{goname}
Version: 0
Release: 0.8%{?dist}
Summary: Golang test utility
License: MIT
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(github.com/chzyer/logex)

%description
%{common_description}


%package    devel
Summary:    %{summary}
BuildArch:  noarch
 
%description devel
%{common_description}
 
This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Mon Nov 12 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0..20180314gita1ea475
- SPEC refresh

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.7.20180314gita1ea475
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gita1ea475
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Mar 14 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.5.20180314gita1ea475
- Fix BuildRequires 

* Thu Mar 08 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.4.20180314gita1ea475
- Update with the new Go packaging

* Tue Feb 13 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20160617gitbea8f08
- Added patch fixing erroneous number of arguments in Errorf function

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.20160617gitbea8f08
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Sep 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.1.20160617gitbea8f08
- First package for Fedora

