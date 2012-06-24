Summary:	A font viewer for Type 1 and TrueType fonts
Summary(pl):	Przegl�darka czcionek Type 1 i TrueType
Name:		gfontview
Version:	0.5.0
Release:	1
License:	GPL
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(es):	X11/Aplicaciones
Group(pl):	X11/Aplikacje
Group(pt_BR):	X11/Aplica��es
Group(pt):	X11/Aplica��es
Source0:	ftp://download.sourceforge.net/pub/sourceforge/gfontview/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-autoconf.patch
Icon:		gfontview.xpm
URL:		http://gfontview.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype1-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	libungif-devel
BuildRequires:	libstdc++-devel
BuildRequires:	t1lib-devel >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

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

%description -l pl
gfontview jest przegl�dark� czcionek (PostScrpit Type 1 i TrueType).
Wy�wietla list� wszystkich czcionek z wybranego katalogu i umo�liwia
podgl�d ka�dej z nich zar�wno w g��wnym oknie programu, jak i w
oddzielnych oknach. Posiada mo�liwo�� wyg�adzania czcionek
(antialiasing), drukowania przyk�ad�w kroju w postaci pojedy�czych
znak�w, linii jak r�wnie� wi�kszych partii tekstu, co pozwala na
zorientowanie si�, jak wygl�da ca�a strona z wykorzystaniem wybranej
czcionki. Program umo�liwia tak�e zapisanie znaku lub fragmentu tekstu
w formacie GIF.

%prep
%setup -q
%patch -p1

%build
gettextize --copy --force
aclocal -I .
automake -a -c
autoconf
autoheader
CXXFLAGS="%{rpmcflags} -I/usr/include/freetype \
	-fno-rtti -fno-exceptions -fno-implicit-templates"
%configure \
	--with-libungif \
	--with-fontdir=/usr/share/fonts/Type1
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/misc,%{_applnkdir}/Utilities}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install gfontviewrc $RPM_BUILD_ROOT%{_datadir}/misc/gfontviewrc
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

gzip -9nf README ChangeLog AUTHORS NEWS TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS,NEWS,TODO}.gz
%attr(755,root,root) %{_bindir}/gfontview

%config(noreplace) %verify(not size mtime md5) %{_datadir}/misc/gfontviewrc
%{_applnkdir}/Utilities/gfontview.desktop
