%define version 0.9.7
Summary: UNFS3 user-space NFSv3 server
Group: Applications/System
Name: unfs3
Version: %{version}
Release: 1
Copyright: BSD
Packager: Pascal Schmidt <der.eremit@email.de>
Vendor: none
Source: unfs3-%{version}.tar.gz
Buildroot: /tmp/unfs3

%prep
%setup

%build
./configure --enable-cluster --prefix=/usr --mandir=/usr/share/man
make

%install
[ -n "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
[ -n "$RPM_BUILD_ROOT" ] && rm -rf "$RPM_BUILD_ROOT"

%description
UNFS3 is a user-space implementation of the NFS (Network File System)
version 3 server specification. It provides a daemon that supports both
the MOUNT and NFS protocol.

%files
%attr (  -, root, root) %doc README LICENSE NEWS
%attr (755, root, root) /usr/sbin/unfsd
%attr (644, root, root) %doc /usr/share/man/man7/tags.7.gz
%attr (644, root, root) %doc /usr/share/man/man8/unfsd.8.gz
