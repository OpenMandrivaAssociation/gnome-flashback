Name:           gnome-flashback
Version:        3.16.1
Release:        1%{?dist}
Summary:        Classic GNOME session

License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeFlashback
Source0:        http://download.gnome.org/sources/%{name}/3.16/%{name}-%{version}.tar.xz
Patch0:         gnome-flashback-wm-prefs-overrides.patch

BuildRequires:  gnome-common
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.2
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.12.0
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
Requires:       gnome-panel
Requires:       gnome-applets
Requires:       metacity
Requires:       notification-daemon
Requires:       upower
Requires:       gnome-keyring
Requires:       gnome-screensaver
Requires:       gnome-settings-daemon
Requires:       gnome-session

%description
GNOME Flashback is a session for GNOME 3 which was initially called
"GNOME Fallback". It provides a similar user experience to the GNOME 2.x
series sessions. The differences to the MATE project is that GNOME
Flashback uses Gtk+3 and tries to follow the current GNOME development
by integrating recent changes of the GNOME libraries.


%prep
%setup -q
%patch0 -p1


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}


%postun
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi


%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :


%files -f %{name}.lang
%doc COPYING NEWS
%{_sysconfdir}/xdg/menus/gnome-flashback-applications.menu
%{_bindir}/gnome-flashback
%{_libexecdir}/gnome-flashback-compiz
%{_libexecdir}/gnome-flashback-metacity
%{_datadir}/applications/gnome-flashback-init.desktop
%{_datadir}/applications/gnome-flashback.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback.gschema.xml
%{_datadir}/gnome-session/sessions/gnome-flashback-compiz.session
%{_datadir}/gnome-session/sessions/gnome-flashback-metacity.session
%{_datadir}/xsessions/gnome-flashback-compiz.desktop
%{_datadir}/xsessions/gnome-flashback-metacity.desktop

%changelog
* Thu Apr 30 2015 Mike DePaulo <mikedep333@gmail.com> - 3.16.1-1
- Upgrade to 3.16.1 (for GNOME 3.16)

* Fri Feb 27 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-4
- Fix for BGO#738562

* Mon Feb 23 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-3
- Requires: gnome-screensaver

* Tue Feb 10 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-2
- Fix deps

* Mon Feb 02 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.14.0-1
- Update for GNOME 3.14.

* Mon Jan 12 2015 Yaakov Selkowitz <yselkowi@redhat.com> - 3.10.0-1
- Initial release.