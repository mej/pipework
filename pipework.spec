Summary: Software-Defined Networking for Linux Containers
Name: pipework
Version: 20150911
Release: 1.mej%{?dist}
License: Apache License, Version 2.0
Group: Applications/System
URL: https://github.com/mej/pipework
Source0: https://raw.githubusercontent.com/mej/pipework/master/pipework
Requires: /bin/sh
Requires: iproute
BuildArch: noarch

%description
Pipework lets you connect together containers in arbitrarily complex scenarios.
Pipework uses cgroups and namespace and works with "plain" LXC containers
(created with lxc-start), and with the awesome Docker.


%prep
%setup -c -T -n %{name}-%{version}
%{__install} %{SOURCE0} .


%install
test -n "%{buildroot}" && %{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m 0755 %{name} %{buildroot}%{_bindir}/%{name}


%files
%defattr(-, root, root, -)
%{_bindir}/%{name}


%changelog
* Fri Sep 11 2015 Michael Jennings <mej@lbl.gov> - 20150911
- Rewrote spec file.
* Fri Jan 23 2015 Oleg Gashev <oleg@gashev.net> - 20150123
- Initial package.
