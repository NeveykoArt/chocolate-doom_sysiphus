Name:       chocolate-doom
Version:    3.0.1
Release:    alt3
Summary:    Conservative DOOM source port
License:    GPL-2.0+
Group:      Games/Arcade
Source0:    %{name}-%{version}.tar.xz
BuildRequires:  gcc make autoconf automake libSDL2-devel libSDL2_mixer-devel libSDL2_net-devel libpng-devel

%description
Chocolate Doom - conservative DOOM source port for modern systems

%prep
%setup -q

%build
autoreconf -fi
./configure --prefix=/usr
make

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -delete

%files
/usr/bin/chocolate-doom
/usr/bin/chocolate-heretic
/usr/bin/chocolate-hexen
/usr/bin/chocolate-strife
/usr/bin/chocolate-server
/usr/bin/chocolate-doom-setup
/usr/bin/chocolate-heretic-setup
/usr/bin/chocolate-hexen-setup
/usr/bin/chocolate-strife-setup
/usr/share/applications/org.chocolate_doom.Doom.desktop
/usr/share/applications/org.chocolate_doom.Heretic.desktop
/usr/share/applications/org.chocolate_doom.Hexen.desktop
/usr/share/applications/org.chocolate_doom.Strife.desktop
/usr/share/applications/org.chocolate_doom.Setup.desktop
/usr/share/applications/screensavers/org.chocolate_doom.Doom_Screensaver.desktop
/usr/share/icons/hicolor/128x128/apps/chocolate-doom.png
/usr/share/icons/hicolor/128x128/apps/chocolate-heretic.png
/usr/share/icons/hicolor/128x128/apps/chocolate-hexen.png
/usr/share/icons/hicolor/128x128/apps/chocolate-strife.png
/usr/share/icons/hicolor/128x128/apps/chocolate-setup.png
/usr/share/metainfo/org.chocolate_doom.Doom.metainfo.xml
/usr/share/metainfo/org.chocolate_doom.Heretic.metainfo.xml
/usr/share/metainfo/org.chocolate_doom.Hexen.metainfo.xml
/usr/share/metainfo/org.chocolate_doom.Strife.metainfo.xml
/usr/share/doc/chocolate-doom/*
/usr/share/doc/chocolate-heretic/*
/usr/share/doc/chocolate-hexen/*
/usr/share/doc/chocolate-strife/*

%changelog
* Sun Apr 05 2026 Artem Neveiko <aneveiko@altlinux.org> 3.0.1-alt3
- Initial package

