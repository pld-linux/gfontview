#
# Conditional build:
%bcond_with	gnome1	# with GNOME (1.x) support
#
Summary:	A font viewer for Type 1 and TrueType fonts
Summary(pl.UTF-8):	Przeglądarka czcionek Type 1 i TrueType
Name:		gfontview
Version:	0.5.0
Release:	7
License:	GPL
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/gfontview/%{name}-%{version}.tar.gz
# Source0-md5:	f06e0e9d67f7d8b3af251fa593e83eeb
Source1:	%{name}.desktop
Patch0:		%{name}-autoconf.patch
Patch1:		%{name}-gcc33.patch
Patch2:		%{name}-po.patch
Patch3:		%{name}-gcc4.patch
URL:		http://gfontview.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype1-devel
BuildRequires:	gettext-devel
BuildRequires:	giflib-devel
%{?with_gnome1:BuildRequires:	gnome-libs-devel}
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	libstdc++-devel
BuildRequires:	t1lib-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gfontview is a Font Viewer for outline fonts (PostScript Type 1 and
TrueType). It displays all fonts present in the chosen directory in a
list, with a preview of the font in the main window. It also allows
you to display a particular character or string of a font in an own
window, this character or string can be antialiased (smoothed). The
displayed character or string can be saved in GIF format. You can also
print a sample of a font. The program can also print a longer text in
the selected font, thus allowing you to get an impresion of how a text
page looks like in the selected font.

%description -l pl.UTF-8
gfontview jest przeglądarką czcionek (PostScrpit Type 1 i TrueType).
Wyświetla listę wszystkich czcionek z wybranego katalogu i umożliwia
podgląd każdej z nich zarówno w głównym oknie programu, jak i w
oddzielnych oknach. Posiada możliwość wygładzania czcionek
(antialiasing), drukowania przykładów kroju w postaci pojedynczych
znaków, linii jak również większych partii tekstu, co pozwala na
zorientowanie się, jak wygląda cała strona z wykorzystaniem wybranej
czcionki. Program umożliwia także zapisanie znaku lub fragmentu tekstu
w formacie GIF.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

%build
%{__gettextize}
%{__aclocal} -I .
%{__autoconf}
%{__autoheader}
%{__automake}
CXXFLAGS="%{rpmcflags} -I/usr/include/freetype \
	-fno-rtti -fno-exceptions -fno-implicit-templates"
%configure \
	SPOOLER="/usr/bin/lpr" \
	--with-fontdir=/usr/share/fonts/Type1 \
	%{!?with_gnome1:--disable-gnome}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/misc,%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install gfontviewrc $RPM_BUILD_ROOT%{_datadir}/misc/gfontviewrc
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog AUTHORS NEWS TODO
%attr(755,root,root) %{_bindir}/gfontview
%config(noreplace) %verify(not md5 mtime size) %{_datadir}/misc/gfontviewrc
%{_desktopdir}/gfontview.desktop
%{_pixmapsdir}/gfontview.png
