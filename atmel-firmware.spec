%define name atmel-firmware
%define version 1.3
%define release %mkrel 1
%define url http://www.thekelleys.org.uk/

Name:		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	Distributable
Group:		System/Kernel and hardware
URL: 		%{url}
Source0: 	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
Summary: 	Firmware for Atmel at76c50x wireless network chips
BuildArch: 	noarch

%description
The drivers for Atmel at76c50x wireless network chipss in the
Linux 2.6.x kernel and at http://at76c503a.berlios.de/ do not 
include the firmware and this firmware needs to be loaded by 
the host on most cards using these chips. 
This package provides the firmware images which 
should be automatically loaded as needed by the hotplug system. It also 
provides a small loader utility which can be used to accomplish the 
same thing when hotplug is not in use. 

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p -m 755 $RPM_BUILD_ROOT/lib/firmware
cp images/* $RPM_BUILD_ROOT/lib/firmware
cp images.usb/* $RPM_BUILD_ROOT/lib/firmware

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README COPYING 
/lib/firmware/*.bin

