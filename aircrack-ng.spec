#
# TODO:
# - PLD it more
# - Find more deps
# - optflags
#
Summary:	Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
Summary(pl.UTF-8):	Pewny sniffer 802.11 (sieci bezprzewodowe) i łamacz kluczy WEP/WPA-PSK
Name:		aircrack-ng
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://download.aircrack-ng.org/%{name}-%{version}.tar.gz
# Source0-md5:	d21ea65caac6c9b47bd058c4e7032292
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
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

for BINARY in \
 aircrack-ng \
 airdecap-ng \
 aireplay-ng \
 airodump-ng \
 airmon-ng \
 ivstools \
 makeivs \
 kstats \
 packetforge-ng
do
	install -m 755 "$BINARY" $RPM_BUILD_ROOT%{_bindir}
	install -m 644 manpages/"$BINARY.1" $RPM_BUILD_ROOT%{_mandir}/man1
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README test patches
%attr(755,root,root) %{_bindir}/aircrack-ng
%attr(755,root,root) %{_bindir}/airdecap-ng
%attr(755,root,root) %{_bindir}/aireplay-ng
%attr(755,root,root) %{_bindir}/airmon-ng
%attr(755,root,root) %{_bindir}/airodump-ng
%attr(755,root,root) %{_bindir}/ivstools
%attr(755,root,root) %{_bindir}/kstats
%attr(755,root,root) %{_bindir}/makeivs
%attr(755,root,root) %{_bindir}/packetforge-ng
%{_mandir}/man1/aircrack-ng.1*
%{_mandir}/man1/airdecap-ng.1*
%{_mandir}/man1/aireplay-ng.1*
%{_mandir}/man1/airmon-ng.1*
%{_mandir}/man1/airodump-ng.1*
%{_mandir}/man1/ivstools.1*
%{_mandir}/man1/kstats.1*
%{_mandir}/man1/makeivs.1*
%{_mandir}/man1/packetforge-ng.1*
