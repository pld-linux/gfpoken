Summary:	BlackBox-type game for GTK inspired by Marble
Summary(pl):	Zainspirowana przez Marble gra dla GTK
Name:		gfpoken
Version:	0.25
Release:	1
License:	GPL
Group:		X11/Applications/Games
Group(de):	X11/Applikationen/Spiele
Group(pl):	X11/Aplikacje/Gry
Source0:	http://gfpoken.bigw.org/%{name}-%{version}.tar.gz
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
automake -a
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir}}

install gfpoken $RPM_BUILD_ROOT%{_bindir}
install iconpix.h $RPM_BUILD_ROOT%{_pixmapsdir}/gfpoken.xpm

gzip -9nf AUTHORS ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
