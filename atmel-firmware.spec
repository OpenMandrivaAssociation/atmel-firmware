Name:		atmel-firmware
Version: 	1.3
Release: 	6
License: 	Distributable
Group:		System/Kernel and hardware
URL: 		https://www.thekelleys.org.uk/
Source0: 	%{name}-%{version}.tar.bz2
Source1:	atmel_at76c504_2958.bin
Source2:	atmel_at76c504a_2958.bin
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
mv images/atmel_at76c504c-wpa.bin images/atmel_at76c504-wpa.bin

%build

%install
mkdir -p -m 755 %{buildroot}/lib/firmware
cp images/* %{buildroot}/lib/firmware
cp images.usb/* %{buildroot}/lib/firmware
cp %{SOURCE1} %{SOURCE2} %{buildroot}/lib/firmware

%files
%doc README COPYING 
/lib/firmware/*.bin
