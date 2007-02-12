Summary:	BlackBox-type game for GTK+ inspired by Marble
Summary(pl.UTF-8):   Zainspirowana przez Marble gra dla GTK+
Name:		gfpoken
Version:	0.25
Release:	5
License:	GPL
Group:		X11/Applications/Games
Source0:	http://gfpoken.bigw.org/%{name}-%{version}.tar.gz
# Source0-md5:	59365bf8fd96ae3e231c57da7aa26c03
Source1:	%{name}.png
Source2:	%{name}.desktop
URL:		http://gfpoken.bigw.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
BlackBox-type game for GTK+ inspired by Marble.

%description -l pl.UTF-8
Zainspirowana przez Marble gra dla GTK+.

%prep
%setup -q

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_desktopdir}}

install gfpoken $RPM_BUILD_ROOT%{_bindir}
install iconpix.h $RPM_BUILD_ROOT%{_pixmapsdir}/gfpoken.xpm

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_pixmapsdir}/*
%{_desktopdir}/*.desktop
