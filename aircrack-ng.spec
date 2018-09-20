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

Summary:	Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
Summary(pl.UTF-8):	Pewny sniffer 802.11 (sieci bezprzewodowe) i łamacz kluczy WEP/WPA-PSK
Name:		aircrack-ng
Version:	1.3
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://download.aircrack-ng.org/%{name}-%{version}.tar.gz
# Source0-md5:	c7c5b076dee0c25ee580b0f56f455623
URL:		http://www.aircrack-ng.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libnl-devel
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pkgconfig
%{?with_sqlite:BuildRequires:	sqlite3-devel}
BuildRequires:	zlib-devel
Requires:	ethtool
Requires:	grep
Requires:	iw
Requires:	usbutils
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

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I build/m4/stubs -I build/m4
%{__autoconf}
%{__automake}
%configure \
	ETHTOOL=/sbin/ethtool \
	--with-openssl \
	--with%{!?with_experimental:out}-experimental \
	--with%{!?with_ext_scripts:out}-ext-scripts \
	--with-%{!?with_sqlite:out}-sqlite3 \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%attr(755,root,root) %ghost %{_libdir}/libaircrack-crypto-x86-avx.so.0
%attr(755,root,root) %{_libdir}/libaircrack-crypto-x86-avx.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libaircrack-crypto-x86-avx2.so.0
%attr(755,root,root) %{_libdir}/libaircrack-crypto-x86-avx2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libaircrack-crypto-x86-sse2.so.0
%attr(755,root,root) %{_libdir}/libaircrack-crypto-x86-sse2.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libaircrack-crypto.so.0
%attr(755,root,root) %{_libdir}/libaircrack-crypto.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libaircrack-osdep.so.0
%attr(755,root,root) %{_libdir}/libaircrack-osdep.so.*.*

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
