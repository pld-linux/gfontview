Summary: A font viewer for Type 1 and TrueType fonts.
Name: gfontview
Version: 0.2.2
Release: 1
Copyright: GPL
Group: X11/Utilities
Source: http://www.geocities.com/SiliconValley/Foothills/1458/gfontview-0-2-2.tgz
URL: http://www.geocities.com/SiliconValley/Foothills/1458/
BuildRoot: /var/tmp/gfontview-root
Vendor: Roberto Alameda <alameda@ibm.net>
Packager: Katherine Lim (Katherine.Lim@infotech.monash.edu.au)
Requires: gtk+ >= 1.2, t1lib >= 0.8, freetype >= 1.2

%description
This is an ALPHA preliminary release.

gfontview is a Font Viewer for outline fonts (PostScript Type 1 and TrueType). 
It will display all fonts present in the chosen directory in a list,
with a preview of the font also present in the main window.

Note: compiled with freetype 1.2 and t1lib 0.8.1 beta

%prep
%setup

%build
export CFLAGS=$RPM_OPT_FLAGS
./configure --prefix=$RPM_BUILD_ROOT/usr
make

%install
make install

%clean
rm -rf $RPM_BUILD_ROOT

%files
/usr/bin/gfontview

%doc AUTHORS COPYING ChangeLog INSTALL NEWS README TODO
