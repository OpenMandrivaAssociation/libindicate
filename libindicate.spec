%define major 5
%define major_gtk 3
%define libname %mklibname indicate %{major}
%define girname %mklibname indicate-gir 0.6
%define gtklibname %mklibname indicate-gtk3_ %{major_gtk}
%define gtkgirname %mklibname indicategtk3-gir 0.6
%define develname %mklibname indicate -d
%define gtkdevelname %mklibname indicate-gtk -d

Name:           libindicate
Version:        0.6.1
Release:        %mkrel 3
Summary:        Library for applications to raise flags on DBus
License:        LGPLv3
Group:          System/Libraries
URL:            https://launchpad.net/libindicate

Source0:        http://launchpad.net/%{name}/0.3/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:		libindicate-0.6.1-glib.patch
Patch1:		libindicate-0.6.1-link.patch
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.76
BuildRequires:	pkgconfig(dbusmenu-glib-0.4) >= 0.3.97
BuildRequires:	pkgconfig(gapi-2.0) >= 2.12.1
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gio-2.0) >= 2.18
BuildRequires:	pkgconfig(glib-2.0) >= 2.18
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(gtk-sharp-2.0) >= 2.12
#BuildRequires:	pkgconfig(mono) >= 1.0
BuildRequires:	pkgconfig(pygobject-2.0) >= 0.22
BuildRequires:	pkgconfig(pygtk-2.0) >= 2.14.0
BuildRequires:	pkgconfig(python) >= 2.3.5
BuildRequires:	vala-tools
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  pkgconfig(gnome-doc-utils)
BuildRequires:	gnome-common
BuildRequires:	intltool

%description
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

#-----------------------------------------------------------------------

%package -n     %{libname}
Summary:        Library for applications to raise flags on DBus
Group:          System/Libraries

%description -n %{libname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n       %{libname}
%{_libdir}/libindicate.so.%{major}*

#-----------------------------------------------------------------------

%package -n     %{gtklibname}
Summary:        Library for applications to raise flags on DBus
Group:          System/Libraries
Obsoletes:	%{_lib}indicate-gtk33 < 0.6.1-2

%description -n %{gtklibname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n       %{gtklibname}
%{_libdir}/libindicate-gtk3.so.%{major_gtk}* 

#-----------------------------------------------------------------------

%package -n	%{girname}
Summary:	GObject Introspection interface description for libindicate
Group:		System/Libraries
Requires:	%{libname} = %{version}

%description -n %{girname}
GObject Introspection interface description for libindicate-gtk.

%files -n       %{girname}
%{_libdir}/girepository-1.0/Indicate-0.6.typelib

#-----------------------------------------------------------------------

%package -n	%{gtkgirname}
Summary:	GObject Introspection interface description for libindicate-gtk
Group:		System/Libraries
Requires:	%{gtklibname} = %{version}

%description -n %{gtkgirname}
GObject Introspection interface description for libindicate-gtk.

%files -n       %{gtkgirname}
%{_libdir}/girepository-1.0/IndicateGtk3-0.6.typelib

#-----------------------------------------------------------------------
%if 0
%package -n     indicate-sharp
Summary:        Library for applications to raise flags on DBus
Group:          Development/Other
Provides:       mono-%{name} = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n indicate-sharp
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n       indicate-sharp
%{_libdir}/pkgconfig/indicate-sharp-0.1.pc
%{_libdir}/indicate-sharp-0.1
%{_prefix}/lib/mono/indicate/indicate-sharp.dll
%{_prefix}/lib/mono/gac/indicate-sharp

#-----------------------------------------------------------------------

%package -n     indicate-gtk-sharp
Summary:        Library for applications to raise flags on DBus
Group:          Development/Other
Provides:       mono-%{name}-gtk = %{version}-%{release}
Requires:       %{gtklibname} = %{version}-%{release}

%description -n	indicate-gtk-sharp
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n       indicate-gtk-sharp
%{_libdir}/pkgconfig/indicate-gtk-sharp-0.1.pc
%{_libdir}/indicate-gtk-sharp-0.1
%{_prefix}/lib/mono/indicate-gtk/indicate-gtk-sharp.dll
%{_prefix}/lib/mono/gac/indicate-gtk-sharp
%endif

#-----------------------------------------------------------------------

%package -n     python-%{name}
Summary:        Library for applications to raise flags on DBus
Group:          Development/Python

%description -n	python-%{name}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n       python-%{name}
%{py_platsitedir}/indicate
%{_datadir}/pygtk/2.0/defs/indicate.defs

#-----------------------------------------------------------------------

%package -n     %{develname}
Summary:        Library headers for %{name}
Group:          Development/C
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n	%{develname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n       %{develname}
%{_includedir}/%{name}-0.6/libindicate
%{_libdir}/libindicate.so
%{_libdir}/pkgconfig/indicate-0.6.pc
%{_datadir}/gir-1.0/Indicate-0.6.gir
%{_datadir}/vala/vapi/Indicate-0.6.vapi

#------------------------------------------------------------------------

%package -n     %{gtkdevelname}
Summary:        Library headers for %{name}
Group:          Development/C
Requires:       %{gtklibname} = %{version}
Requires:       %{develname} = %{version}
Provides:       %{name}-gtk-devel = %{version}-%{release}

%description -n %{gtkdevelname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n       %{gtkdevelname}
%{_includedir}/%{name}-0.6/libindicate-gtk/
%{_libdir}/libindicate-gtk3.so
%{_libdir}/pkgconfig/indicate-gtk3-0.6.pc
%{_datadir}/gir-1.0/IndicateGtk3-0.6.gir
%{_datadir}/vala/vapi/IndicateGtk3-0.6.vapi

#-----------------------------------------------------------------------

%package doc
Summary:        Documentation for %{name} 
Group:          Development/C

%description doc
This package provides documentation files for %{name}

%files doc
%doc AUTHORS COPYING COPYING.LGPL.2.1
%{_defaultdocdir}/%{name}/
%{_datadir}/gtk-doc/html/%{name}

#-----------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p0

%build
NOCONFIGURE=yes gnome-autogen.sh
%configure2_5x --disable-static
%make

%install
%makeinstall_std

rm -f %buildroot%_libdir/*.la

%changelog
* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0.4.4-2mdv2011.0
+ Revision: 661476
- mass rebuild

* Tue Jan 04 2011 John Balcaen <mikala@mandriva.org> 0.4.4-1mdv2011.0
+ Revision: 628534
- Update to 0.4.4

* Fri Nov 05 2010 Funda Wang <fwang@mandriva.org> 0.4.1-3mdv2011.0
+ Revision: 593684
- disable introspection
- rebuild for py2.7

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.4.1-2mdv2011.0
+ Revision: 564214
- correct packag ename of indicate-gtk
- add requires on libpackage to mono bindings
- BR libdbusmenu-tools
- New version 0.4.1

* Wed Mar 17 2010 John Balcaen <mikala@mandriva.org> 0.3.6-2mdv2010.1
+ Revision: 522709
- Fix BuildRequires (missing libdbumenu-devel)
- Update to 0.3.6
- Update to 0.3.4
- update major (now 4)
- add buildrequires on libdbusmenu
- cosmetic changes on spec

* Thu Dec 31 2009 John Balcaen <mikala@mandriva.org> 0.2.3-3mdv2010.1
+ Revision: 484270
- Split libindicate-devel in libindicate-devel & libindicate-gtk-devel

* Mon Dec 14 2009 John Balcaen <mikala@mandriva.org> 0.2.3-2mdv2010.1
+ Revision: 478685
- Add patch0 (disable build of examples & tests files)
- add examples & tests folder in -doc package

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - fix layout

* Wed Dec 09 2009 John Balcaen <mikala@mandriva.org> 0.2.3-1mdv2010.1
+ Revision: 475355
- import libindicate


