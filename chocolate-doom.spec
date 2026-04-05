Name:       chocolate-doom
Version:    3.0.1
Release:    alt1
Summary:    Conservative DOOM source port
License:    GPL-2.0+
Group:      Games/Arcade
Source0:    https://www.chocolate-doom.org/downloads/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc make libSDL2-devel libSDL2_mixer-devel libSDL2_net-devel libpng-devel

%description
Chocolate Doom — точная реплика оригинального DOOM для современных систем.
Максимальная совместимость с оригиналом, включая баги и ограничения.

%prep
%setup -q

%build
./configure --prefix=/usr
make

%install
make install DESTDIR=%{buildroot}

# Убираем .la файлы, которые не нужны в Alt Linux
find %{buildroot} -name '*.la' -delete

%files
/usr/bin/chocolate-doom
/usr/bin/chocolate-setup
/usr/bin/chocolate-server
/usr/share/man/man6/chocolate-doom.6*
/usr/share/man/man6/chocolate-setup.6*
/usr/share/man/man5/chocolate-doom.cfg.5*
/usr/share/applications/chocolate-doom.desktop
/usr/share/icons/hicolor/*/apps/chocolate-doom.png
/usr/share/doc/chocolate-doom/*

%changelog
* Sun Apr 05 2026 Artem Neveiko <aneveiko@altlinux.org> 3.0.1-alt1
- Initial package for Alt Linux
