%global pypi_name temperusb
%global pypi_version 1.6.0

%global __python_requires null

Name:           python-%{pypi_name}
Version:        %{pypi_version}
Release:        3%{?dist}
Summary:        Reads temperature from TEMPerV1 devices (USB 0c45:7401)

License:        GPLv3
URL:            https://github.com/padelt/temper-python
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%description
This is a rewrite of a userspace USB driver for TEMPer devices presenting a USB
ID like this: 0c45:7401 Microdia My device came from [M-Ware ID7747]( and also
reports itself as 'RDing TEMPerV1.2'.Also provides a passpersist-module for
NetSNMP (as found in the snmpd packages of Debian and Ubuntu) to present the
temperature of 1-3 USB devices via SNMP.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(pyusb)
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
This is a rewrite of a userspace USB driver for TEMPer devices presenting a USB
ID like this: 0c45:7401 Microdia My device came from [M-Ware ID7747]( and also
reports itself as 'RDing TEMPerV1.2'.Also provides a passpersist-module for
NetSNMP (as found in the snmpd packages of Debian and Ubuntu) to present the
temperature of 1-3 USB devices via SNMP. Reported working devices| USB ID |
Name...


%prep
%autosetup -n %{pypi_name}-%{pypi_version}
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%license LICENSE.md
%doc README.md
%{_bindir}/temper-poll
%{_bindir}/temper-snmp
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{pypi_version}-py%{python3_version}.egg-info

%changelog
* Tue Jan 31 2023 Lars Kiesow <lkiesow@uos.de> - 1.6.0-2
- pyusb version requirement

* Mon Jan 30 2023 Lars Kiesow <lkiesow@uos.de> - 1.6.0-1
- Initial package.
