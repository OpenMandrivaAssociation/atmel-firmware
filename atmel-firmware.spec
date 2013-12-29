Name:		atmel-firmware%
Version: 	1.3
Release: 	6
License: 	Distributable
Group:		System/Kernel and hardware
URL: 		http://www.thekelleys.org.uk/
Source0: 	%{name}-%{version}.tar.bz2
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
mkdir -p -m 755 %{buildroot}/lib/firmware
cp images/* %{buildroot}/lib/firmware
cp images.usb/* %{buildroot}/lib/firmware

%files
%doc README COPYING 
/lib/firmware/*.bin
