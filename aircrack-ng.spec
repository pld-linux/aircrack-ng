#
# TODO:
# - PLD it more
# - Find more deps
# - optflags
#
Summary:	Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
Summary(pl):	Pewny sniffer 802.11 (sieci bezprzewodowe) i ³amacz kluczy WEP/WPA-PSK
Name:		aircrack-ng
Version:	0.6
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://download.aircrack-ng.org/%{name}-%{version}.tar.gz
# Source0-md5:	6b85fe925c93c972f3d9f8170dce46c6
URL:		http://www.aircrack-ng.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
aircrack-ng is a set of tools for auditing wireless networks. It's an
enhanced/reborn version of aircrack. It consists of airodump-ng (an
802.11 packet capture program), aireplay-ng (an 802.11 packet
injection program), aircrack (static WEP and WPA-PSK cracking),
airdecap-ng (decrypts WEP/WPA capture files), and some tools to handle
capture files (merge, convert, etc.).

%description -l pl
aircrack-ng jest zestawew narzêdzi do audytów sieci bezprzewodowych.
Jest to ulepszona/odnowiona wersja aircracka. Sk³ada sie z programów
airodump-ng (do przechwytywania pakietów 802.11), aireplay-ng (do
wstrzykiwania pakietów 802.11), aircrack (do statycznego ³amania WEP i
WPA-PSK), airdecap-ng (do odszyfrowywania przechwyconych plików
WEP/WPA) i paru narzêdzi do obs³ugi plików przechwytów (merge,
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
 arpforge-ng \
 airmon-ng \
 ivstools
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
%attr(755,root,root) %{_bindir}/airodump-ng
%attr(755,root,root) %{_bindir}/arpforge-ng
%attr(755,root,root) %{_bindir}/airmon-ng
%attr(755,root,root) %{_bindir}/ivstools
%{_mandir}/man1/aircrack-ng.1*
%{_mandir}/man1/airdecap-ng.1*
%{_mandir}/man1/aireplay-ng.1*
%{_mandir}/man1/airodump-ng.1*
%{_mandir}/man1/arpforge-ng.1*
%{_mandir}/man1/airmon-ng.1*
%{_mandir}/man1/ivstools.1*
