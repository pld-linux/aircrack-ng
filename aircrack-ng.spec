#
# TODO:
# - PLD it more
# - Find more deps
# - optflags
# - cflags
# - sbin/bin - change to bin?
#

%define		relc	-rc1
Summary:	Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
Summary(pl.UTF-8):	Pewny sniffer 802.11 (sieci bezprzewodowe) i łamacz kluczy WEP/WPA-PSK
Name:		aircrack-ng
Version:	1.0
Release:	0.rc1.1
License:	GPL
Group:		Applications/Networking
Source0:	http://download.aircrack-ng.org/%{name}-%{version}%{relc}.tar.gz
# Source0-md5:	113f0be4a2454f5c73cec25412b20f64
Patch0:		%{name}-mandir.patch
URL:		http://www.aircrack-ng.org/
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
%setup -qn %{name}-%{version}%{relc}
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" 
#	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
        prefix=%{_prefix} \
        DESTDIR=$RPM_BUILD_ROOT

echo MANDIR %{mandir}
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README test patches
%attr(755,root,root) %{_bindir}/aircrack-ng
%attr(755,root,root) %{_bindir}/airdecap-ng
%attr(755,root,root) %{_bindir}/buddy-ng
%attr(755,root,root) %{_bindir}/ivstools
%attr(755,root,root) %{_bindir}/kstats
%attr(755,root,root) %{_bindir}/makeivs-ng
%attr(755,root,root) %{_bindir}/packetforge-ng
%attr(755,root,root) %{_sbindir}/airbase-ng
%attr(755,root,root) %{_sbindir}/airdriver-ng
%attr(755,root,root) %{_sbindir}/aireplay-ng
%attr(755,root,root) %{_sbindir}/airmon-ng
%attr(755,root,root) %{_sbindir}/airodump-ng
%attr(755,root,root) %{_sbindir}/airserv-ng
%attr(755,root,root) %{_sbindir}/airtun-ng
%attr(755,root,root) %{_sbindir}/easside-ng
%attr(755,root,root) %{_sbindir}/patchchk
%attr(755,root,root) %{_sbindir}/wesside-ng
%{_mandir}/man1/aircrack-ng.1*
%{_mandir}/man1/airdecap-ng.1*
%{_mandir}/man1/airdriver-ng.1*
%{_mandir}/man1/aireplay-ng.1*
%{_mandir}/man1/airmon-ng.1*
%{_mandir}/man1/airodump-ng.1*
%{_mandir}/man1/airolib-ng.1*
%{_mandir}/man1/airsev-ng.1*
%{_mandir}/man1/airtun-ng.1*
%{_mandir}/man1/buddy-ng.1*
%{_mandir}/man1/easside-ng.1*
%{_mandir}/man1/ivstools.1*
%{_mandir}/man1/kstats.1*
%{_mandir}/man1/makeivs-ng.1*
%{_mandir}/man1/packetforge-ng.1*
%{_mandir}/man1/wesside-ng.1*
