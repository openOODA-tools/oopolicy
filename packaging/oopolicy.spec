Name:           oopolicy
Version:        0.1.0
Release:        1%{?dist}
Summary:        Validates capability policy manifests before launching agent subtasks.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oopolicy
Source0:        oopolicy-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oopolicy is a sovereign, capability-bounded POLICY VERIFIER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oopolicy
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oopolicy-uninstall

%files
/usr/bin/oopolicy
/usr/bin/oopolicy-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
