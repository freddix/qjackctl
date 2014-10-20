Summary:	Simple application to control the JACK server
Name:		qjackctl
Version:	0.3.12
Release:	1
License:	GPL
Group:		X11/Applications/Sound
Source0:	http://downloads.sourceforge.net/qjackctl/%{name}-%{version}.tar.gz
# Source0-md5:	441800d633f0b1fb767ba4320f25f638
Patch0:		%{name}-desktop.patch
URL:		http://qjackctl.sourceforge.net
BuildRequires:	QtDBus-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	jack-audio-connection-kit-devel
BuildRequires:	qt-linguist
Requires(post,postun):	gtk+-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	jack-audio-connection-kit
Provides:	jack-patch-bay
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qjackctl is a Qt application to control the JACK sound server.
Provides a simple GUI dialog for setting several JACK parameters.

%prep
%setup -q
%patch0 -p1

# use comman qt locale location
sed -i "s|@localedir@|%{_datadir}/qt/translations|" Makefile.in

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --without-mo --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/*/apps/qjackctl.png
%{_mandir}/man1/qjackctl.1*

