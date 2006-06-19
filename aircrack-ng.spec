#
# TODO:
# - PLD it more
# - Find more deps
# - automake it for God's sake
#
Summary:	Reliable 802.11 (wireless) sniffer and WEP/WPA-PSK key cracker
Name:		aircrack-ng
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://freshmeat.net/redir/aircrack-ng/63481/url_tgz/%{name}-%{version}.tar.gz
# Source0-md5:	303daa6f1b030f8f9a2f00542051b96c
URL:		http://www.aircrack-ng.org
Requires:	glibc >= 2
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
Jest to ulepszona/odnowiona wersja aircracka. Sk³ada sie z airodump-ng
(program przechwytywania pakietów 802.11), aireplay-ng (program do
wstrzykiwania pakietów 802.11), aircrack (statyczne ³amanie WEP i
WPA-PSK), airdecap-ng (odzyfrowywanie przechwyconych plików WEP/WPA),
i parê narzêdzi do obs³ugi plików przechwytów (merge, convert, etc.).

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d 	$RPM_BUILD_ROOT%{_bindir} \
		$RPM_BUILD_ROOT%{_mandir}/man1

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
%{_mandir}/man1/aircrack-ng.*
%{_mandir}/man1/airdecap-ng.*
%{_mandir}/man1/aireplay-ng.*
%{_mandir}/man1/airodump-ng.*
%{_mandir}/man1/arpforge-ng.*
%{_mandir}/man1/airmon-ng.*
%{_mandir}/man1/ivstools.*
