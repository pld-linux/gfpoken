Summary:	BlackBox-type game for GTK inspired by Marble
Summary(pl):	Zainspirowana przez Marble gra dla GTK
Name:		gfpoken
Version:	0.25
Release:	2
License:	GPL
Group:		X11/Applications/Games
Group(cs):	X11/Aplikace/Hry
Group(da):	X11/Programmer/Spil
Group(de):	X11/Applikationen/Spiele
Group(es):	X11/Aplicaciones/Juegos
Group(fr):	X11/Applications/Jeux
Group(it):	X11/Applicazioni/Giochi
Group(ja):	X11/•¢•◊•Í•±°º•∑•Á•Û/•≤°º•‡
Group(no):	X11/Applikasjoner/Spill
Group(pl):	X11/Aplikacje/Gry
Group(pt):	X11/AplicaÁıes/Jogos
Group(ru):	X11/“…Ãœ÷≈Œ…—/È«“Ÿ
Group(sv):	X11/Till‰mpningar/Spel
Source0:	http://gfpoken.bigw.org/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://gfpoken.bigw.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
BlackBox-type game for GTK inspired by Marble.

%description -l pl
Zainspirowana przez Marble gra dla GTK.

%prep
%setup -q

%build
rm -f missing
aclocal
autoconf
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_applnkdir}/Games}

install gfpoken $RPM_BUILD_ROOT%{_bindir}
install iconpix.h $RPM_BUILD_ROOT%{_pixmapsdir}/gfpoken.xpm

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games

gzip -9nf AUTHORS ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_applnkdir}/Games/*
