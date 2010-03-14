%define name libindicate
%define version 0.3.6
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
Patch0:		libindicate-0.2.3-mdv-disable-build-of-tests-examples.patch
License:	LGPLv3
Group:		System/Libraries
URL:		https://launchpad.net/libindicate
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	glib2-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libxml2-devel
BuildRequires:	libgdk_pixbuf2.0-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-doc
BuildRequires:	gnome-doc-utils
BuildRequires:	pkgconfig

%description
A small library for applications to raise "flags" on DBus for other
components of the desktop to pick up and visualize. Currently used by
the messaging indicator.

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
%patch0 -p0

%build
%configure2_5x 
%make

%install
%__rm -rf %{buildroot}
%makeinstall
# Copying examples & test files to doc dire
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/
%__cp -fr examples %{buildroot}/%{_defaultdocdir}/%{name}/
%__cp -fr tests %{buildroot}/%{_defaultdocdir}/%{name}/

%clean
%__rm -rf %{buildroot}
