# kubernetes

## Description

This repository contains spec files for building `kubernetes` RPM packages and its ecosystem.

Packages are built and published by [spec-package-builder](https://github.com/damex-el-packages/spec-package-builder) pipeline.

Currently, packages and their corresponding spec files are built and tested only for `Red Hat Enterprise Linux 9`, `Red Hat Enterprise Linux 10` and its derivatives like `Alma Linux 9`, `Alma Linux 10`, `Rocky Linux 9` and `Rocky Linux 10`.

[Follow here if you want to use prebuilt packages](#Using-prebuilt-packages).

## Using prebuilt packages

### Add damex-kubernetes repository with prebuilt packages

To add `damex-kubernetes` repository to `Red Hat Enterprise Linux 9` install the following package:

```sh
# x86_64
https://yum-repositories.damex.org/kubernetes/el/9/x86_64/damex-kubernetes-release-0.3.0-1.el9.x86_64.rpm
# aarch64
https://yum-repositories.damex.org/kubernetes/el/9/aarch64/damex-kubernetes-release-0.3.0-1.el9.aarch64.rpm
```

To add `damex-kubernetes` repository to `Red Hat Enterprise Linux 10` install the following package:

```sh
# x86_64
https://yum-repositories.damex.org/kubernetes/el/10/x86_64/damex-kubernetes-release-0.3.0-1.el10.x86_64.rpm
# aarch64
https://yum-repositories.damex.org/kubernetes/el/10/aarch64/damex-kubernetes-release-0.3.0-1.el10.aarch64.rpm
```

Alternatively, it can be done manually by adding the following configuration to `/etc/yum.repos.d/damex-kubernetes.repo`:

```sh
[damex-kubernetes]
name = damex-kubernetes
baseurl = https://yum-repositories.damex.org/kubernetes/el/$releasever/$basearch
gpgcheck = 1
repo_gpgcheck = 1
gpgkey = https://yum-repositories.damex.org/kubernetes/kubernetes-2036-09-25.asc
```

### List of prebuilt packages

| Package              | Repository | Architecture | Distributives              |
|----------------------|------------|--------------|----------------------------|
| cni-plugins          | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| cni-plugins-ipam     | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| cni-plugins-main     | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| cni-plugins-meta     | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| etcd                 | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| etcd-benchmark       | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| etcd-dump-db         | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| etcd-dump-logs       | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| etcd-dump-metrics    | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| etcd-etcdctl         | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| etcd-etcdutl         | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| flannel              | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| helm                 | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| kube-apiserver       | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| kube-controller-manager | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| kube-proxy           | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| kube-router          | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| kube-scheduler       | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| kubectl              | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| kubectl-convert      | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
| kubelet              | damex-kubernetes | x86_64, aarch64 | Red Hat Enterprise Linux 9, Red Hat Enterprise Linux 10 |
