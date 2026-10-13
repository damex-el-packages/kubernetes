%define debug_package %{nil}

Name: damex-kubernetes-release
Version: 0.3.0
Release: 1%{?dist}
Summary: damex kubernetes repository configuration
License: MIT
URL: https://yum-repositories.damex.org
BuildArch: noarch

%description

%prep

%build

%install
%{__install} -d %{buildroot}%{_sysconfdir}/yum.repos.d
%{__cat} <<'EOF' > %{buildroot}%{_sysconfdir}/yum.repos.d/damex-kubernetes.repo
[damex-kubernetes]
name = damex-kubernetes
baseurl = https://yum-repositories.damex.org/kubernetes/el/$releasever/$basearch
gpgcheck = 1
repo_gpgcheck = 1
gpgkey = https://yum-repositories.damex.org/kubernetes/kubernetes-2036-09-25.asc
EOF

%files
%defattr(-,root,root,-)
%config %{_sysconfdir}/yum.repos.d/damex-kubernetes.repo

%changelog
* %(date -u +"%%a %%b %%d %%Y") Roman Kuzmitskii <el-packages@damex.org> - %{version}-%{release}
- History: https://github.com/damex-el-packages/kubernetes/commits/production
