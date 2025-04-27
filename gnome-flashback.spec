Name:           gnome-flashback
Version:        3.56.0
Release:        1
Summary:        Classic GNOME session
Group:		Graphical desktop/GNOME
License:        GPLv3+
URL:            https://wiki.gnome.org/Projects/GnomeFlashback
Source0:        https://download.gnome.org/sources/gnome-flashback/3.52/%{name}-%{version}.tar.xz

BuildRequires:  gnome-common
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(xkbfile)
BuildRequires:	pkgconfig(xkeyboard-config)
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.15.2
BuildRequires:  pkgconfig(gnome-desktop-3.0) >= 3.12.0
BuildRequires:	pkgconfig(gnome-bluetooth-3.0)
BuildRequires:	pkgconfig(libgnome-panel)
BuildRequires:  pkgconfig(gsettings-desktop-schemas)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(polkit-agent-1)
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(upower-glib) >= 0.99.0
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(gdm)
BuildRequires:  pkgconfig(xxf86vm)
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
%autopatch -p1

%build
%configure
%make_build

%install
%make_install

%find_lang %{name}

%postun
if [ $1 -eq 0 ] ; then
    glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans
glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files -f %{name}.lang
%doc COPYING NEWS README.md
%{_sysconfdir}/xdg/menus/gnome-flashback-applications.menu
%{_sysconfdir}/xdg/autostart/gnome-flashback-nm-applet.desktop
%{_sysconfdir}/xdg/autostart/gnome-flashback-clipboard.desktop
%{_sysconfdir}/xdg/autostart/gnome-flashback-media-keys.desktop
%{_sysconfdir}/xdg/autostart/gnome-flashback-idle-monitor.desktop
%{_sysconfdir}/xdg/autostart/%{name}-polkit.desktop
%{_sysconfdir}/xdg/autostart/gnome-flashback-geoclue-demo-agent.desktop
%{_bindir}/gnome-flashback
%{_libdir}/gnome-panel/modules/system_indicators.so
%{_libexecdir}/gnome-flashback-metacity
%{_libexecdir}/gnome-flashback-clipboard
%{_libexecdir}/gnome-flashback-media-keys
%{_libexecdir}/gnome-flashback-idle-monitor
%{_libexecdir}/%{name}-polkit
%{_datadir}/applications/gnome-flashback.desktop
%{_datadir}/gnome-session/sessions/gnome-flashback-metacity.session
%{_datadir}/xsessions/gnome-flashback-metacity.desktop
%{_datadir}/desktop-directories/X-GNOME-Flashback-Settings-System.directory
%{_datadir}/desktop-directories/X-GNOME-Flashback-Settings.directory
%{_datadir}/glib-2.0/schemas/00_gnome-flashback.gschema.override
%{_datadir}/glib-2.0/schemas/org.gnome.gnome-flashback*
%{_datadir}/gnome-panel/layouts/gnome-flashback.layout
%{_datadir}/gnome-control-center/keybindings/50-gnome-flashback-screenshots.xml
%{_datadir}/desktop-directories/X-GNOME-Flashback-Science.directory
%{_userunitdir}/gnome-flashback.service
%{_userunitdir}/gnome-flashback.target
%{_userunitdir}/gnome-session@gnome-flashback-metacity.target.d/session.conf
