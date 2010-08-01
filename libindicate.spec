%define name libindicate
%define version 0.4.1
%define release %mkrel 1
%define summary Library for applications to raise flags on DBus
%define major 4
%define major_gtk 2
%define libname %mklibname indicate %{major}
%define gtklibname  %mklibname indicate %{major_gtk}-gtk
%define develname %mklibname indicate -d
%define gtkdevelname %mklibname indicate-gtk -d

Summary:	%summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://launchpad.net/%{name}/0.3/%{version}/+download/%{name}-%{version}.tar.gz
#Add patch0 to disable building of files provided in examples & tests folder
Patch0:		libindicate-0.4.1-mdv-disable-build-of-tests-examples.patch
Patch1:		libindicate-0.4.1-link.patch
License:	LGPLv3
Group:		System/Libraries
URL:		https://launchpad.net/libindicate
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	glib2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libdbusmenu-devel >= 0.3.8
Buildrequires:	libdbusmenu-tools
BuildRequires:	libxml2-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	gtk+2-devel
BuildRequires:	vala-tools
BuildRequires:	gobject-introspection-devel
BuildRequires:	mono-devel
BuildRequires:	python-devel
BuildRequires:	pygtk2.0-devel
BuildRequires:	gtk-sharp2
BuildRequires:	gtk-sharp2-devel
BuildRequires:	gtk-doc
BuildRequires:	gnome-doc-utils
BuildRequires:	pkgconfig

%description
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

#-----------------------------------------------------------------------

%package -n	%{libname}
Summary:	Library for applications to raise flags on DBus
Group:		System/Libraries

%description -n	%{libname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n	%{libname}
%defattr(-,root,root)
%{_libdir}/libindicate.so.%{major}*

#-----------------------------------------------------------------------

%package -n	%{gtklibname}
Summary:	Library for applications to raise flags on DBus
Group:		System/Libraries

%description -n	%{gtklibname}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n	%{gtklibname}
%defattr(-,root,root)
%{_libdir}/libindicate-gtk.so.%{major_gtk}* 

#-----------------------------------------------------------------------

%package -n	indicate-sharp
Summary:	Library for applications to raise flags on DBus
Group:		Development/Other
Provides:	mono-%{name} = %{version}-%{release}

%description -n indicate-sharp
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n	indicate-sharp
%defattr(-,root,root)
%{_libdir}/pkgconfig/indicate-sharp-0.1.pc
%{_libdir}/indicate-sharp-0.1
%{_prefix}/lib/mono/indicate/indicate-sharp.dll
%{_prefix}/lib/mono/gac/indicate-sharp

#-----------------------------------------------------------------------

%package -n	indicate-gtk-sharp
Summary:	Library for applications to raise flags on DBus
Group:		Development/Other
Provides:	mono-%{name}-gtk = %{version}-%{release}

%description -n	indicate-gtk-sharp
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n	indicate-gtk-sharp
%defattr(-,root,root)
%{_libdir}/pkgconfig/indicate-gtk-sharp-0.1.pc
%{_libdir}/indicate-gtk-sharp-0.1
%{_prefix}/lib/mono/indicate-gtk/indicate-gtk-sharp.dll
%{_prefix}/lib/mono/gac/indicate-gtk-sharp

#-----------------------------------------------------------------------

%package -n	python-%{name}
Summary:	Library for applications to raise flags on DBus
Group:		Development/Python

%description -n	python-%{name}
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

%files -n	python-%{name}
%defattr(-,root,root)
%{py_platsitedir}/indicate
%{_datadir}/pygtk/2.0/defs/indicate.defs

#-----------------------------------------------------------------------

%package -n	%{develname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n	%{develname}
%defattr(-,root,root)
%{_includedir}/%{name}-0.2/libindicate
%{_libdir}/libindicate.so
%{_libdir}/libindicate.a
%{_libdir}/libindicate.la  
%{_libdir}/pkgconfig/indicate.pc
%{_libdir}/girepository-1.0/Indicate-0.2.typelib
%{_datadir}/gir-1.0/Indicate-0.2.gir
%{_datadir}/vala/vapi/Indicate-0.2.vapi

#------------------------------------------------------------------------

%package -n     %{gtkdevelname}
Summary:	Library headers for %{name}
Group:		Development/C
Requires:	%{gtklibname} = %{version}
Requires:	%{develname} = %{version}
Provides:	%{name}-gtk-devel = %{version}-%{release}
Conflicts:	 %{develname} < 0.2.3-3

%description -n %{gtkdevelname}
This is the libraries, include files and other resources you can use
to incorporate %{name} into applications.

%files -n       %{gtkdevelname}
%defattr(-,root,root)
%{_includedir}/%{name}-0.2/libindicate-gtk/
%{_libdir}/libindicate-gtk.so
%{_libdir}/libindicate-gtk.a
%{_libdir}/libindicate-gtk.la
%{_libdir}/pkgconfig/indicate-gtk.pc
%{_libdir}/girepository-1.0/Indicate-Gtk-0.2.typelib
%{_datadir}/gir-1.0/Indicate-Gtk-0.2.gir
%{_datadir}/vala/vapi/Indicate-Gtk-0.2.vapi

#-----------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name} 
Group:		Development/C
Requires:	%{libname} = %{version}

%description doc
This package provides documentation files for %{name}

%files doc
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.LGPL.2.1
%{_defaultdocdir}/%{name}/
%{_datadir}/gtk-doc/html/%{name}

#-----------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0 -b .build
%patch1 -p0 -b .link

%build
autoreconf -fi
%configure2_5x 
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
# Copying examples & test files to doc dire
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/
%__cp -fr examples %{buildroot}/%{_defaultdocdir}/%{name}/
%__cp -fr tests %{buildroot}/%{_defaultdocdir}/%{name}/

%clean
%__rm -rf %{buildroot}
