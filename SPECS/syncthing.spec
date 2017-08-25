Name:		syncthing
Version:	0.14.36
Release:	0%{?dist}
Summary:	Open, trustworthy and decentralized sync
# Set to amd64 or 386
%define arch	amd64
%define InVersion	0.8.7

Group:		Applications/System
License:	MPLv2
URL:		https://github.com/syncthing/syncthing
Source0:	https://github.com/syncthing/syncthing/releases/download/v%{version}/syncthing-linux-%{arch}-v%{version}.tar.gz
Source1:	https://github.com/syncthing/syncthing-inotify/releases/download/v%{InVersion}/syncthing-inotify-linux-%{arch}-v%{InVersion}.tar.gz

Requires:	policycoreutils-python

%description
Syncthing replaces proprietary sync and cloud services with something open,
trustworthy and decentralized. Your data is your data alone and you deserve
to choose where it is stored, if it is shared with some third party and how
it's transmitted over the Internet.

%prep
tar -zxf %{SOURCE0}
cd syncthing-linux-%{arch}-v%{version}/
tar -zxf %{SOURCE1}

%install
mkdir -p %{buildroot}/usr/bin/
cd syncthing-linux-%{arch}-v%{version}/
cp syncthing-inotify %{buildroot}/usr/bin/
cp syncthing %{buildroot}/usr/bin/

%if 0%{?rhel}  == 6
mkdir -p %{buildroot}/etc/init.d/
cp /root/supportfiles/syncthing  %{buildroot}/etc/init.d/
%else
mkdir -p %{buildroot}/etc/systemd/system/
cp /root/supportfiles/linux-systemd/system/syncthing\@.service %{buildroot}/etc/systemd/system/
cp /root/supportfiles/linux-systemd/system/syncthing-resume.service %{buildroot}/etc/systemd/system/
cp /root/supportfiles/linux-systemd/system/syncthing-inotify\@.service %{buildroot}/etc/systemd/system/
mkdir -p %{buildroot}/etc/systemd/user/
cp /root/supportfiles/linux-systemd/user/syncthing.service %{buildroot}/etc/systemd/user/
cp /root/supportfiles/linux-systemd/user/syncthing-inotify.service %{buildroot}/etc/systemd/user/
%endif

mkdir -p %{buildroot}/etc/syncthing/
cp /root/supportfiles/config.xml  %{buildroot}/etc/syncthing/

%files
%defattr(-,root,root)
/usr/bin/syncthing
/usr/bin/syncthing-inotify
%if 0%{?rhel}  == 6
/etc/init.d/syncthing
%else
/etc/systemd/system/syncthing@.service
/etc/systemd/system/syncthing-inotify@.service
/etc/systemd/system/syncthing-resume.service
/etc/systemd/user/syncthing.service
/etc/systemd/user/syncthing-inotify.service
%endif
/etc/syncthing/config.xml

%changelog
* Thu Aug  24 2017 Trevor Hartman <trevor@hydrobuilder.com>
- Bump syncthing version 0.14.27 -> 0.14.36

* Thu Jun  1 2017 Trevor Hartman <trevor@hydrobuilder.com>
- Bump syncthing version 0.14.23 -> 0.14.27

* Thu Feb  9 2017 Pierre-Alain TORET <pierre-alain.toret@protonmail.com>
- Bump syncthing version 0.14.7 -> 0.14.23

* Thu Sep 22 2016 Logan Owen <logan@s1network.com>
- Bump syncthing version 0.13.1 -> 0.14.7

* Mon Feb 08 2016 Martin Lazarov <martin@lazarov.bg>
- Initial spec version
