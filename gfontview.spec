Summary:	A font viewer for Type 1 and TrueType fonts
Summary(pl):	Przegl±darka czcionek Type 1 i TrueType
Name:		gfontview
Version:	0.3.2
Release:	2
License:	GPL
Group:		X11/Utilities
Group(pl):	X11/Narzêdzia
Source0:	http://www.geocities.com/SiliconValley/Foothills/1458/%{name}-0_3_2.tgz
Source1:	gfontview.desktop
Patch0:		gfontview-autoconf.patch
Icon:		gfontview.xpm
URL:		http://www.geocities.com/SiliconValley/Foothills/1458/index.html
BuildRequires:	xpm-devel
BuildRequires:	gtk+-devel >= 1.2.6
BuildRequires:	t1lib-devel >= 1.0.0
BuildRequires:	freetype-devel
BuildRequires:	libungif-devel
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
gfontview is a Font Viewer for outline fonts (PostScript Type 1 and TrueType).
It displays all fonts present in the chosen directory in a list, with a preview
of the font in the main window. It also allows you to display a particular
character or string of a font in an own window, this character or string can be
antialiased (smoothed). The displayed character or string can be saved in GIF
format. You can also print a sample of a font.  The program can also print a
longer text in the selected font, thus allowing you to get an impresion of how
a text page looks like in the selected font.

%description -l pl
gfontview jest przegl±dark± czcionek (PostScrpit Type 1 i TrueType).
Wy¶wietla listê wszystkich czcionek z wybranego katalogu i umo¿liwia podgl±d
ka¿dej z nich zarówno w g³ównym oknie programu, jak i w oddzielnych oknach.
Posiada mo¿liwo¶æ wyg³adzania czcionek (antialiasing), drukowania przyk³adów
kroju w postaci pojedyñczych znaków, linii jak równie¿ wiêkszych partii
tekstu, co pozwala na zorientowanie siê, jak wygl±da ca³a strona z
wykorzystaniem wybranej czcionki. Program umo¿liwia tak¿e zapisanie znaku
lub fragmentu tekstu w formacie GIF.


%prep
%setup -q
%patch -p1

%build
aclocal -I .
automake
autoconf
autoheader
LDFLAGS="-s"
CXXFLAGS="$RPM_OPT_FLAGS -I/usr/include/freetype -fno-rtti -fno-exceptions -fno-implicit-templates"
export LDFLAGS CXXFLAGS
%configure \
	--with-libungif \
	--with-fontdir=/usr/share/fonts/Type1
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/misc,%{_applnkdir}/Utilities}

make install DESTDIR=$RPM_BUILD_ROOT

install .gfontviewrc $RPM_BUILD_ROOT%{_datadir}/misc/gfontviewrc
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities

gzip -9nf README ChangeLog AUTHORS NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,ChangeLog,AUTHORS,NEWS,TODO}.gz
%attr(755,root,root) %{_bindir}/gfontview

%config(noreplace) %verify(not size mtime md5) %{_datadir}/misc/gfontviewrc
%{_applnkdir}/Utilities/gfontview.desktop
