%define name libindicate
%define version 0.2.3
%define release %mkrel 1
%define summary Library for applications to raise flags on DBus
%define major 3
%define major_gtk 1
%define libname %mklibname indicate %{major}
%define gtklibname  %mklibname indicate %{major_gtk}-gtk
%define develname %mklibname indicate -d

Summary:	%summary
Name:		%name
Version:	%version
Release:	%release
Source0:	http://launchpad.net/%{name}/0.2/%{version}/+download/%{name}-%{version}.tar.gz
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
%doc AUTHORS COPYING COPYING.LGPL.2.1
%{_libdir}/im-client
%{_libdir}/indicate-alot
%{_libdir}/indicate-and-crash
%{_libdir}/libindicate.so.3
%{_libdir}/libindicate.so.3.0.2
%{_libdir}/listen-and-print
%{_libdir}/show-hide-server
%{_libdir}/test-indicator-display-client
%{_libdir}/test-indicator-display-half-client
%{_libdir}/test-indicator-display-half-server
%{_libdir}/test-indicator-display-server
%{_libdir}/test-interests-client
%{_libdir}/test-interests-server
%{_libdir}/test-interests-server1
%{_libdir}/test-interests-server2
%{_libdir}/test-interests-server3
%{_libdir}/test-interests-server4
%{_libdir}/test-interests-server5
%{_libdir}/test-max-indicators-client
%{_libdir}/test-max-indicators-server
%{_libdir}/test-max-indicators-server-repeat
%{_libdir}/test-simple-client
%{_libdir}/test-simple-server
%{_libdir}/test-thousand-indicators-client
%{_libdir}/test-thousand-indicators-server

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
%{_libdir}/libindicate-gtk.so.1 
%{_libdir}/libindicate-gtk.so.1.0.0 
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
%{_includedir}/%{name}-0.2/
%{_libdir}/libindicate.so
%{_libdir}/libindicate.a
%{_libdir}/libindicate.la  
%{_libdir}/libindicate-gtk.so
%{_libdir}/libindicate-gtk.a
%{_libdir}/libindicate-gtk.la
%{_libdir}/pkgconfig/indicate-gtk.pc
%{_libdir}/pkgconfig/indicate.pc

#-----------------------------------------------------------------------

%package doc
Summary:	Documentation for %{name} 
Group:		Development/C
Requires:	%{libname} = %{version}

%description doc
This package provides documentation files for %{name}

%files doc
%defattr(-,root,root)
%{_defaultdocdir}/%{name}/
%{_datadir}/gtk-doc/html/%{name}

#-----------------------------------------------------------------------

%prep
%setup -q 

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall

%clean
%__rm -rf %{buildroot}
