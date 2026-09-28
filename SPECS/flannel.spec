%define debug_package %{nil}
%undefine source_date_epoch_from_changelog

Name: flannel
Version: 0.28.1
Release: 1%{?dist}
Summary: simple and easy way to configure a layer 3 network fabric designed for Kubernetes
License: ASL 2.0
URL: https://github.com/flannel-io/flannel
Source: https://github.com/flannel-io/flannel/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires: golang >= 1.26.0, golang < 1.27.0

%description
Flannel is a simple and easy way to configure a layer 3 network fabric designed for Kubernetes.

%prep
%autosetup

%build
export GOFLAGS=-buildvcs=false
go mod download
go build -o $(pwd)/flanneld

%install
%{__install} -d %{buildroot}%{_bindir}
%{__install} -m 755 flanneld %{buildroot}%{_bindir}/flanneld

%files
%defattr(-,root,root,-)
%{_bindir}/flanneld
