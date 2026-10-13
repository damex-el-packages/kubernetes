%define debug_package %{nil}

Name: helm
Version: 3.20.1
Release: 1%{?dist}
Summary: The package manager for Kubernetes
License: Apache-2.0
URL: https://helm.sh
Source: https://github.com/helm/helm/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: golang >= 1.26.0, golang < 1.27.0
BuildRequires: go-rpm-macros

%description
Helm is a tool for managing Charts. Charts are packages of pre-configured Kubernetes resources.

%prep
%autosetup

%build
export GOFLAGS=-buildvcs=false
export GO111MODULE=on
go mod download
%gobuild -o $(pwd)/helm ./cmd/helm

%install
%{__install} -d %{buildroot}%{_bindir}
%{__install} -m 755 helm %{buildroot}%{_bindir}/helm

%files
%defattr(-,root,root,-)
%{_bindir}/helm

%changelog
* %(date -u +"%%a %%b %%d %%Y") Roman Kuzmitskii <el-packages@damex.org> - %{version}-%{release}
- History: https://github.com/damex-el-packages/kubernetes/commits/production
