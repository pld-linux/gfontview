Summary:	A font viewer for Type 1 and TrueType fonts
Summary(pl):	Przegl±darka czcionek Type 1 i TrueType
Name:		gfontview
Version:	0.3.0
Release:	1
Copyright:      GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source0:	http://www.geocities.com/SiliconValley/Foothills/1458/%{name}-0_3_0.tgz
Source1:	gfontview.desktop
Icon:           gfontview.xpm
Patch:		gfontview-fproto.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildPrereq:	gtk+-devel >= 1.2.0
BuildPrereq:	glib-devel >= 1.2.0
BuildPrereq:	t1lib-devel
BuildPrereq:	freetype-devel
BuildPrereq:	libungif-devel
BuildRoot:   	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
gfontview is a Font Viewer for outline fonts (PostScript Type 1 and TrueType). 
It displays all fonts present in the chosen directory in a list, with 
a preview of the font in the main window. It also allows you to display 
a particular character or string of a font in an own window, this character 
or string can be antialiased (smoothed). The displayed character or string 
can be saved in GIF format. You can also print a sample of a font. 
The program can also print a longer text in the selected font, thus allowing 
you to get an impresion of how a text page looks like in the selected font.


%description -l pl
gfontview jest przegl±dark± czcionek (PostScrpit Type 1 i TrueType).
Wy¶wietla listê wszystkich czcionek z wybranego katalogu i umo¿liwia
podgl±d ka¿dej z nich zarówno w g³ównym oknie programu, jak i w oddzielnych
oknach. Posiada mo¿liwo¶æ wyg³adzania czcionek (antialiasing), drukowania
przyk³adów kroju w postaci pojedyñczych znaków, linii jak równie¿ wiêkszych
partii tekstu, co pozwala na zorientowanie siê, jak wygl±da ca³a strona 
z wykorzystaniem wybranej czcionki. Program umo¿liwia tak¿e zapisanie
znaku lub fragmentu tekstu w formacie GIF.

%prep
%setup -q
%patch -p0

%build
CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--with-libungif
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/etc/X11/applnk/Utilities

make install-strip DESTDIR=$RPM_BUILD_ROOT
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Utilities

gzip -9nf README ChangeLog AUTHORS NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS,NEWS,TODO}.gz
%attr(755,root,root) %{_bindir}/gfontview

/etc/X11/applnk/Utilities/gfontview.desktop
