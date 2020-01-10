# As soon as EVRD macro really works I won't disable linting.Sflo:
# lib64indicate-devel.x86_64: E: no-dependency-on (Badness: 1) lib64indicate-devel/lib64indicate-devel-libs/liblib64indicate-devel
# lib64indicate-gtk3-devel.x86_64: E: no-dependency-on (Badness: 1) lib64indicate-gtk3-devel/lib64indicate-gtk3-devel-libs/liblib64indicate-gtk3-devel

%define _build_pkgcheck_set %{nil}

%define api	0.6
%define major	5
%define libname %mklibname indicate %{major}
%define girname %mklibname indicate-gir %{api}
%define devname %mklibname indicate -d

%define gtk3maj	3
%define libgtk3 %mklibname indicate-gtk3_ %{gtk3maj}
%define girgtk3 %mklibname indicategtk3-gir %{api}
%define devgtk3 %mklibname indicate-gtk3 -d

Summary:	Library for applications to raise flags on DBus
Name:		libindicate
Version:	0.6.1
Release:	11
License:	LGPLv3
Group:		System/Libraries
Url:		https://launchpad.net/libindicate
Source0:	http://launchpad.net/%{name}/%{api}/%{version}/+download/%{name}-%{version}.tar.gz
Patch0:		libindicate-0.6.1-glib.patch
Patch1:		libindicate-0.6.1-link.patch
Patch2:		libindicate-automake-1.13.patch

BuildRequires:	gtk-doc
BuildRequires:	gnome-common
BuildRequires:	intltool
BuildRequires:	vala-tools
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.76
BuildRequires:	pkgconfig(dbusmenu-glib-0.4) >= 0.3.97
BuildRequires:	pkgconfig(gapi-2.0) >= 2.12.1
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gio-2.0) >= 2.18
BuildRequires:	pkgconfig(glib-2.0) >= 2.18
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.0
BuildRequires:	pkgconfig(gtk-sharp-2.0) >= 2.12
#BuildRequires:	pkgconfig(mono) >= 1.0
BuildRequires:	pkgconfig(pygobject-2.0) >= 0.22
BuildRequires:	pkgconfig(pygtk-2.0) >= 2.14.0
BuildRequires:	pkgconfig(python2) >= 2.3.5
BuildRequires: gcc-c++, gcc, gcc-cpp

%description
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%package -n     %{libname}
Summary:	Library for applications to raise flags on DBus
Group:		System/Libraries

%description -n %{libname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%package -n	%{girname}
Summary:	GObject Introspection interface description for libindicate
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for libindicate-gtk.

%package -n     %{devname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Requires:	%{girname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%package -n     %{libgtk3}
Summary:	Library for applications to raise flags on DBus
Group:		System/Libraries
Obsoletes:	%{_lib}indicate-gtk33 < 0.6.1-2

%description -n %{libgtk3}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%package -n	%{girgtk3}
Summary:	GObject Introspection interface description for libindicate-gtk
Group:		System/Libraries

%description -n %{girgtk3}
GObject Introspection interface description for libindicate-gtk.

%package -n     %{devgtk3}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libgtk3} = %{EVRD}
Requires:	%{girgtk3} = %{EVRD}
Provides:	%{name}-gtk3-devel = %{EVRD}
Obsoletes:	%{_lib}indicate-gtk-devel < 0.6.1-5

%description -n %{devgtk3}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%if 0
%package -n     indicate-sharp
Summary:	Library for applications to raise flags on DBus
Group:		Development/Other
Provides:	mono-%{name} = %{EVRD}
Requires:	%{libname} = %{EVRD}

%description -n indicate-sharp
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%package -n     indicate-gtk-sharp
Summary:	Library for applications to raise flags on DBus
Group:		Development/Other
Provides:	mono-%{name}-gtk = %{EVRD}
Requires:	%{libgtk3} = %{EVRD}

%description -n	indicate-gtk-sharp
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.
%endif

%package -n     python-%{name}
Summary:	Library for applications to raise flags on DBus
Group:		Development/Python

%description -n	python-%{name}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%package doc
Summary:	Documentation for %{name} 
Group:		Development/C

%description doc
This package provides documentation files for %{name}

%prep
%setup -q
%autopatch -p1
NOCONFIGURE=yes gnome-autogen.sh

%build
export CC=gcc
export CXX=g++
perl -pi -e "s|-lpyglib-2.0-python|-lpyglib-2.0-python2|" configure

%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files -n       %{libname}
%{_libdir}/libindicate.so.%{major}*

%files -n       %{girname}
%{_libdir}/girepository-1.0/Indicate-%{api}.typelib

%files -n       %{devname}
%{_includedir}/%{name}-%{api}/libindicate
%{_libdir}/libindicate.so
%{_libdir}/pkgconfig/indicate-%{api}.pc
%{_datadir}/gir-1.0/Indicate-%{api}.gir
%{_datadir}/vala/vapi/Indicate-%{api}.vapi

%files -n       %{libgtk3}
%{_libdir}/libindicate-gtk3.so.%{gtk3maj}* 

%files -n       %{girgtk3}
%{_libdir}/girepository-1.0/IndicateGtk3-%{api}.typelib

%files -n       %{devgtk3}
%{_includedir}/%{name}-%{api}/libindicate-gtk/
%{_libdir}/libindicate-gtk3.so
%{_libdir}/pkgconfig/indicate-gtk3-%{api}.pc
%{_datadir}/gir-1.0/IndicateGtk3-%{api}.gir
%{_datadir}/vala/vapi/IndicateGtk3-%{api}.vapi

%if 0
%files -n       indicate-sharp
%{_libdir}/pkgconfig/indicate-sharp-0.1.pc
%{_libdir}/indicate-sharp-0.1
%{_prefix}/lib/mono/indicate/indicate-sharp.dll
%{_prefix}/lib/mono/gac/indicate-sharp

%files -n       indicate-gtk-sharp
%{_libdir}/pkgconfig/indicate-gtk-sharp-0.1.pc
%{_libdir}/indicate-gtk-sharp-0.1
%{_prefix}/lib/mono/indicate-gtk/indicate-gtk-sharp.dll
%{_prefix}/lib/mono/gac/indicate-gtk-sharp
%endif

%files -n       python-%{name}
%{py2_platsitedir}/indicate
%{_datadir}/pygtk/2.0/defs/indicate.defs

%files doc
%doc AUTHORS COPYING COPYING.LGPL.2.1
%{_defaultdocdir}/%{name}/
%{_datadir}/gtk-doc/html/%{name}

