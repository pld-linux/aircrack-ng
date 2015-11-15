#
# TODO:
# - PLD it more
# - Find more deps
# - optflags
# - cflags
# - sbin/bin - change to bin?
# - package airdrop-ng and airgraph-ng
#
Summary:	Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
Summary(pl.UTF-8):	Pewny sniffer 802.11 (sieci bezprzewodowe) i łamacz kluczy WEP/WPA-PSK
Name:		aircrack-ng
Version:	1.2
%define	subver	rc2
%define	rel	0.1
Release:	%{subver}.%{rel}
License:	GPL
Group:		Applications/Networking
Source0:	http://download.aircrack-ng.org/%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	ebe9d537f06f4d6956213af09c4476da
URL:		http://www.aircrack-ng.org/
BuildRequires:	libnl-devel
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
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
%setup -q -n %{name}-%{version}-%{subver}

sed -i -e 's#-Werror -O3#$(PLDFLAGS)#g' common.mak

%build
%{__make} -j1 \
	CC="%{__cc}" \
	PLDFLAGS="%{rpmcppflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
        prefix=%{_prefix} \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README test patches
%attr(755,root,root) %{_bindir}/aircrack-ng
%attr(755,root,root) %{_bindir}/airdecap-ng
%attr(755,root,root) %{_bindir}/airdecloak-ng
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
%attr(755,root,root) %{_sbindir}/airserv-ng
%attr(755,root,root) %{_sbindir}/airtun-ng
%{_mandir}/man1/aircrack-ng.1*
%{_mandir}/man1/airdecap-ng.1*
%{_mandir}/man1/airdecloak-ng.1*
%{_mandir}/man1/besside-ng-crawler.1*
%{_mandir}/man1/ivstools.1*
%{_mandir}/man1/kstats.1*
%{_mandir}/man1/makeivs-ng.1*
%{_mandir}/man1/packetforge-ng.1*
%{_mandir}/man1/wpaclean.1*
%{_mandir}/man8/airbase-ng.8*
%{_mandir}/man8/aireplay-ng.8*
%{_mandir}/man8/airmon-ng.8*
%{_mandir}/man8/airodump-ng-oui-update.8*
%{_mandir}/man8/airodump-ng.8*
%{_mandir}/man8/airserv-ng.8*
%{_mandir}/man8/airtun-ng.8*
%{_mandir}/man8/besside-ng.8*
