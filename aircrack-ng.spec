#
# TODO:
# - PLD it more
# - sbin/bin - change to bin?
# - finish ext_scripts bcond:
# -- check python related BR and R
# -- fix packaging python releated stuff
# -- create subpackage for airoscript
# -- fix directory for airoscript*.conf files
# -- fix installation of airoscript desktop files
#
# Conditional build:
%bcond_without	sqlite			# build without sqlite support
%bcond_without	experimental
%bcond_with	ext_scripts		# build with extra scripts (NFY)
%define		lib_ver		1.7.0

Summary:	Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
Summary(pl.UTF-8):	Pewny sniffer 802.11 (sieci bezprzewodowe) i łamacz kluczy WEP/WPA-PSK
Name:		aircrack-ng
Version:	1.7
Release:	2
License:	GPL
Group:		Applications/Networking
Source0:	https://download.aircrack-ng.org/%{name}-%{version}.tar.gz
# Source0-md5:	a918ea7146f91d8c799fb770c38f4bec
URL:		http://www.aircrack-ng.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1:1.14
BuildRequires:	hwloc-devel
BuildRequires:	libgcrypt-devel >= 1.2.0
BuildRequires:	libnl-devel >= 1:3.2
BuildRequires:	libpcap-devel
BuildRequires:	libstdc++-devel >= 6:4.8.1
BuildRequires:	libtool
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
BuildRequires:	python3
BuildRequires:	rpmbuild(macros) >= 2.007
%{?with_sqlite:BuildRequires:	sqlite3-devel}
BuildRequires:	zlib-devel
Requires:	awk
Requires:	coreutils
Requires:	ethtool
Requires:	grep
Requires:	iproute2
Requires:	iw
Requires:	libnl >= 1:3.2
Requires:	pciutils
Requires:	usbutils
Requires:	util-linux
Requires:	virtual(module-tools)
Suggests:	wireless-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aircrack-ng is a set of tools for auditing wireless networks. It's an
enhanced/reborn version of aircrack. It consists of airodump-ng (an
802.11 packet capture program), aireplay-ng (an 802.11 packet
injection program), aircrack (static WEP and WPA-PSK cracking),
airdecap-ng (decrypts WEP/WPA capture files), and some tools to handle
capture files (merge, convert, etc.).

%description -l pl.UTF-8
aircrack-ng jest zestawem narzędzi do audytów sieci bezprzewodowych.
Jest to ulepszona/odnowiona wersja aircracka. Składa sie z programów
airodump-ng (do przechwytywania pakietów 802.11), aireplay-ng (do
wstrzykiwania pakietów 802.11), aircrack (do statycznego łamania WEP i
WPA-PSK), airdecap-ng (do odszyfrowywania przechwyconych plików
WEP/WPA) i paru narzędzi do obsługi plików przechwytów (merge,
convert, etc.).

%package devel
Summary:	Development files for %{name}
Summary(pl.UTF-8):	Pliki deweloperskie dla %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for %{name}.

%description devel -l pl.UTF-8
Pliki deweloperskie dla %{name}

%prep
%setup -q
# Force python3 interpreter
grep -r -l '#!/usr/bin/env python' scripts | xargs sed -i -e 's|#!/usr/bin/env python|#!%{__python3}|g'

%build
%{__libtoolize}
%{__aclocal} -I build/m4/stubs -I build/m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON=%{__python3} \
	ETHTOOL=/sbin/ethtool \
	--disable-silent-rules \
	--with-gcrypt \
	--enable-libnl \
	--with%{!?with_experimental:out}-experimental \
	--with%{!?with_ext_scripts:out}-ext-scripts \
	--without-opt \
	--with%{!?with_sqlite:out}-sqlite3

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f \( -name "*.la" -o -name "*.a" \) -delete -print

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README test patches
%attr(755,root,root) %{_bindir}/aircrack-ng
%attr(755,root,root) %{_bindir}/airdecap-ng
%attr(755,root,root) %{_bindir}/airdecloak-ng
%{?with_sqlite:%attr(755,root,root) %{_bindir}/airolib-ng}
%attr(755,root,root) %{_bindir}/ivstools
%attr(755,root,root) %{_bindir}/kstats
%attr(755,root,root) %{_bindir}/makeivs-ng
%attr(755,root,root) %{_bindir}/packetforge-ng
%attr(755,root,root) %{_bindir}/wpaclean
%attr(755,root,root) %{_sbindir}/airbase-ng
%attr(755,root,root) %{_sbindir}/aireplay-ng
%attr(755,root,root) %{_sbindir}/airmon-ng
%attr(755,root,root) %{_sbindir}/airodump-ng
%attr(755,root,root) %{_sbindir}/airodump-ng-oui-update
%attr(755,root,root) %{_sbindir}/airventriloquist-ng
%attr(755,root,root) %{_sbindir}/airserv-ng
%attr(755,root,root) %{_sbindir}/airtun-ng
%attr(755,root,root) %{_libdir}/libaircrack-ce-wpa-%{lib_ver}.so
%attr(755,root,root) %{_libdir}/libaircrack-ce-wpa.so
%ifarch %{ix86} %{x8664} x32
%attr(755,root,root) %{_libdir}/libaircrack-ce-wpa-x86-avx-%{lib_ver}.so
%attr(755,root,root) %{_libdir}/libaircrack-ce-wpa-x86-avx2-%{lib_ver}.so
%attr(755,root,root) %{_libdir}/libaircrack-ce-wpa-x86-avx2.so
%attr(755,root,root) %{_libdir}/libaircrack-ce-wpa-x86-avx.so
%attr(755,root,root) %{_libdir}/libaircrack-ce-wpa-x86-sse2-%{lib_ver}.so
%attr(755,root,root) %{_libdir}/libaircrack-ce-wpa-x86-sse2.so
%endif
%ifarch %{arm_with_neon}
%attr(755,root,root) %{_libdir}/libaircrack-ce-wpa-arm-neon-%{lib_ver}.so
%attr(755,root,root) %{_libdir}/libaircrack-ce-wpa-arm-neon.so
%endif
%attr(755,root,root) %{_libdir}/libaircrack-osdep-%{lib_ver}.so
%attr(755,root,root) %{_libdir}/libaircrack-osdep.so

%{_mandir}/man1/aircrack-ng.1*
%{_mandir}/man1/airdecap-ng.1*
%{_mandir}/man1/airdecloak-ng.1*
%{?with_sqlite:%{_mandir}/man1/airolib-ng.1*}
%{_mandir}/man1/besside-ng-crawler.1*
%{_mandir}/man1/ivstools.1*
%{_mandir}/man1/kstats.1*
%{_mandir}/man1/makeivs-ng.1*
%{_mandir}/man1/packetforge-ng.1*
%{_mandir}/man1/wpaclean.1*
%{_mandir}/man8/airbase-ng.8*
%{_mandir}/man8/aireplay-ng.8*
%{_mandir}/man8/airventriloquist-ng.8*
%{_mandir}/man8/airmon-ng.8*
%{_mandir}/man8/airodump-ng-oui-update.8*
%{_mandir}/man8/airodump-ng.8*
%{_mandir}/man8/airserv-ng.8*
%{_mandir}/man8/airtun-ng.8*

%if %{with experimental}
%attr(755,root,root) %{_bindir}/besside-ng-crawler
%attr(755,root,root) %{_bindir}/buddy-ng
%attr(755,root,root) %{_sbindir}/besside-ng
%attr(755,root,root) %{_sbindir}/easside-ng
%attr(755,root,root) %{_sbindir}/tkiptun-ng
%attr(755,root,root) %{_sbindir}/wesside-ng
%{_mandir}/man1/buddy-ng.1*
%{_mandir}/man8/besside-ng.8*
%{_mandir}/man8/easside-ng.8*
%{_mandir}/man8/tkiptun-ng.8*
%{_mandir}/man8/wesside-ng.8*
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}
