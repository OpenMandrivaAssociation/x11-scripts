Name:		x11-scripts
Version:	1.0.1
Release:	12
Summary:	Scripts for X
Group:		Development/X11
License:	MIT
Source:		http://xorg.freedesktop.org/releases/individual/app/scripts-%{version}.tar.bz2
Patch0:		xauth_switch_to_sun-des_bash.patch
BuildRequires:	pkgconfig(x11)
BuildRequires:	x11-util-macros >= 1.0.1
BuildArch:	noarch

%description
This package mainly provides xon which starts an X program on a remote machine
using rsh, remsh, or rcmd.

%prep
%setup -q -n scripts-%{version}
%patch0 -p1

%build
%configure2_5x	--x-includes=%{_includedir}\
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


%changelog
* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-9mdv2011.0
+ Revision: 671227
- mass rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-8mdv2011.0
+ Revision: 524367
- rebuilt for 2010.1

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.0.1-7mdv2009.1
+ Revision: 351251
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-6mdv2009.0
+ Revision: 226010
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-5mdv2008.1
+ Revision: 179640
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - fix summary-not-capitalized
    - fix no-buildroot-tag
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 1.0.1-4mdv2008.0
+ Revision: 75688
- manpages is not .bz2 anymore
- rebuild


* Wed May 31 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-31 18:32:34 (31796)
- rebuild to fix cooker uploading

* Mon May 29 2006 Andreas Hasenack <andreas@mandriva.com>
+ 2006-05-29 14:36:37 (31646)
- renamed mdv to packages because mdv is too generic and it's hosting only packages anyway

* Tue May 23 2006 Thierry Vignaud <tvignaud@mandriva.com>
+ 2006-05-23 22:34:52 (31402)
- fill in more missing descriptions

* Thu May 04 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-05-04 21:25:17 (26918)
- increment release

* Thu Apr 27 2006 Gustavo Pichorim Boiko <boiko@mandriva.com>
+ 2006-04-27 04:02:05 (26704)
- Adding X.org 7.0 to the repository

