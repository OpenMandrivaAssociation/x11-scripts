Name:		x11-scripts
Version:	1.0.1
Release:	20
Summary:	Scripts for X
Group:		Development/X11
License:	MIT
Source:		http://xorg.freedesktop.org/releases/individual/app/scripts-%{version}.tar.bz2
Patch0:		xauth_switch_to_sun-des_bash.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-util-macros >= 1.0.1
BuildArch:		noarch

%description
This package mainly provides xon which starts an X program on a remote machine
using rsh, remsh, or rcmd.

%prep
%setup -q -n scripts-%{version}
%patch0 -p1

%build
%configure \
		--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files
%doc COPYING
%{_bindir}/xon
%{_bindir}/fontprop.sh
%{_bindir}/xauth_switch_to_sun-des-1
%{_bindir}/fontname.sh
%{_mandir}/man1/xon.1x*

