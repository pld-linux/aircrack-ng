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
%bcond_without	pcre			# build without pcre support
%bcond_without	experimental
%bcond_with	ext_scripts		# build with extra scripts (NFY)

%define	subver	rc2
%define	rel	0.1
Summary:	Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
Summary(pl.UTF-8):	Pewny sniffer 802.11 (sieci bezprzewodowe) i łamacz kluczy WEP/WPA-PSK
Name:		aircrack-ng
Version:	1.2
Release:	%{subver}.%{rel}
License:	GPL
Group:		Applications/Networking
Source0:	http://download.aircrack-ng.org/%{name}-%{version}-%{subver}.tar.gz
# Source0-md5:	ebe9d537f06f4d6956213af09c4476da
URL:		http://www.aircrack-ng.org/
Patch0:		install.patch
Patch1:		pldflags.patch
Patch2:		install_besside_manual.patch
BuildRequires:	libnl-devel
BuildRequires:	openssl-devel
%{?with_pcre:BuildRequires:	pcre-devel}
BuildRequires:	pkgconfig
%{?with_sqlite:BuildRequires:	sqlite3-devel}
BuildRequires:	zlib-devel
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
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} -j1 \
	%{?with_experimental: experimental=true} \
	%{?with_ext_scripts: ext_scripts=true} \
	%{?with_pcre: pcre=true} \
	%{?with_sqlite: sqlite=true} \
	CC="%{__cc}" \
	PLDFLAGS="%{rpmcppflags} %{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	%{?with_experimental: experimental=true} \
	%{?with_ext_scripts: ext_scripts=true} \
	%{?with_pcre: pcre=true} \
	%{?with_sqlite: sqlite=true} \
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
%attr(755,root,root) %{_sbindir}/airserv-ng
%attr(755,root,root) %{_sbindir}/airtun-ng
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
%{_mandir}/man8/airmon-ng.8*
%{_mandir}/man8/airodump-ng-oui-update.8*
%{_mandir}/man8/airodump-ng.8*
%{_mandir}/man8/airserv-ng.8*
%{_mandir}/man8/airtun-ng.8*

%if %{with experimental}
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
