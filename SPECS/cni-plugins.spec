%define debug_package %{nil}
%define cni_bindir /opt/cni/bin

Name: cni-plugins
Version: 1.9.1
Release: 1%{?dist}
Summary: CNI network plugins
License: Apache-2.0
URL: https://github.com/containernetworking/plugins
Source: https://github.com/containernetworking/plugins/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Requires: cni-plugins-main = %{version}
Requires: cni-plugins-ipam = %{version}
Requires: cni-plugins-meta = %{version}
BuildRequires: golang >= 1.26.0, golang < 1.27.0
BuildRequires: go-rpm-macros

%package -n cni-plugins-main
Summary: CNI network plugins (main)

%package -n cni-plugins-ipam
Summary: CNI network plugins (ipam)

%package -n cni-plugins-meta
Summary: CNI network plugins (meta)

%description
CNI network plugins

%description -n cni-plugins-main
CNI network plugins (main)

%description -n cni-plugins-ipam
CNI network plugins (ipam)

%description -n cni-plugins-meta
CNI network plugins (meta)

%prep
%autosetup -n plugins-%{version}

%build
cd %{_builddir}/plugins-%{version}
export GOFLAGS=-buildvcs=false
export GO111MODULE=on
go mod download
# main
%gobuild -o $(pwd)/bridge ./plugins/main/bridge
%gobuild -o $(pwd)/dummy ./plugins/main/dummy
%gobuild -o $(pwd)/host-device ./plugins/main/host-device
%gobuild -o $(pwd)/ipvlan ./plugins/main/ipvlan
%gobuild -o $(pwd)/loopback ./plugins/main/loopback
%gobuild -o $(pwd)/macvlan ./plugins/main/macvlan
%gobuild -o $(pwd)/ptp ./plugins/main/ptp
%gobuild -o $(pwd)/tap ./plugins/main/tap
%gobuild -o $(pwd)/vlan ./plugins/main/vlan
# ipam
%gobuild -o $(pwd)/dhcp ./plugins/ipam/dhcp
%gobuild -o $(pwd)/host-local ./plugins/ipam/host-local
%gobuild -o $(pwd)/static ./plugins/ipam/static
# meta
%gobuild -o $(pwd)/bandwidth ./plugins/meta/bandwidth
%gobuild -o $(pwd)/firewall ./plugins/meta/firewall
%gobuild -o $(pwd)/portmap ./plugins/meta/portmap
%gobuild -o $(pwd)/sbr ./plugins/meta/sbr
%gobuild -o $(pwd)/tuning ./plugins/meta/tuning
%gobuild -o $(pwd)/vrf ./plugins/meta/vrf

%install
%{__install} -d %{buildroot}%{cni_bindir}
# main
%{__install} -m 755 bridge %{buildroot}%{cni_bindir}/bridge
%{__install} -m 755 dummy %{buildroot}%{cni_bindir}/dummy
%{__install} -m 755 host-device %{buildroot}%{cni_bindir}/host-device
%{__install} -m 755 ipvlan %{buildroot}%{cni_bindir}/ipvlan
%{__install} -m 755 loopback %{buildroot}%{cni_bindir}/loopback
%{__install} -m 755 macvlan %{buildroot}%{cni_bindir}/macvlan
%{__install} -m 755 ptp %{buildroot}%{cni_bindir}/ptp
%{__install} -m 755 tap %{buildroot}%{cni_bindir}/tap
%{__install} -m 755 vlan %{buildroot}%{cni_bindir}/vlan
# ipam
%{__install} -m 755 dhcp %{buildroot}%{cni_bindir}/dhcp
%{__install} -m 755 host-local %{buildroot}%{cni_bindir}/host-local
%{__install} -m 755 static %{buildroot}%{cni_bindir}/static
# meta
%{__install} -m 755 bandwidth %{buildroot}%{cni_bindir}/bandwidth
%{__install} -m 755 firewall %{buildroot}%{cni_bindir}/firewall
%{__install} -m 755 portmap %{buildroot}%{cni_bindir}/portmap
%{__install} -m 755 sbr %{buildroot}%{cni_bindir}/sbr
%{__install} -m 755 tuning %{buildroot}%{cni_bindir}/tuning
%{__install} -m 755 vrf %{buildroot}%{cni_bindir}/vrf

%files

%files -n cni-plugins-main
%defattr(-,root,root,-)
%dir %{cni_bindir}
%{cni_bindir}/bridge
%{cni_bindir}/dummy
%{cni_bindir}/host-device
%{cni_bindir}/ipvlan
%{cni_bindir}/loopback
%{cni_bindir}/macvlan
%{cni_bindir}/ptp
%{cni_bindir}/tap
%{cni_bindir}/vlan

%files -n cni-plugins-ipam
%defattr(-,root,root,-)
%dir %{cni_bindir}
%{cni_bindir}/dhcp
%{cni_bindir}/host-local
%{cni_bindir}/static

%files -n cni-plugins-meta
%defattr(-,root,root,-)
%dir %{cni_bindir}
%{cni_bindir}/bandwidth
%{cni_bindir}/firewall
%{cni_bindir}/portmap
%{cni_bindir}/sbr
%{cni_bindir}/tuning
%{cni_bindir}/vrf

%changelog
* %(date -u +"%%a %%b %%d %%Y") Roman Kuzmitskii <el-packages@damex.org> - %{version}-%{release}
- History: https://github.com/damex-el-packages/kubernetes/commits/production
