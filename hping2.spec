Summary:	A software to do TCP/IP stack auditing and much more
Summary(pl):	Oprogramowanie do audytu stosu TCP/IP
Name:		hping2
%define		_rc	rc3
Version:	2.0.0
Release:	5
License:	GPL/BSD
Group:		Networking/Utilities
#Source0Download:	http://www.hping.org/download.html
Source0:	http://www.hping.org/hping%{version}-%{_rc}.tar.gz
# Source0-md5:	029bf240f2e0545b664b2f8b9118d9e8
Patch0:		%{name}-pcap.patch
URL:		http://www.hping.org/
BuildRequires:	libpcap-devel >= 2:0.8.1
Provides:	hping
Obsoletes:	hping
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hping is a network tool able to send custom ICMP/UDP/TCP packets and
to display target replies like ping do with ICMP replies. hping
handle fragmentation, arbitrary packet body and size and can be used
in order to transfer files under supported protocols.

%description -l pl
hping to narz�dzie sieciowe do wysy�ania w�asnych pakiet�w
ICMP/UDP/TCP i wy�wietlania odpowiedzi, podobnie jak robi to ping z
odpowiedziami ICMP. hping obs�uguje fragmentacj�, dowolne zawarto�ci
i rozmiary pakiet�w i mo�e by� u�ywany do przesy�ania plik�w przez
obs�ugiwane protoko�y.

%prep
%setup -q -n %{name}-%{_rc}
%patch0 -p1

%build
MANPATH="%{_mandir}" \

%ifarch ppc sparc ppc64 sparc64 sparcv9
%define byteorder	-DBYTE_ORDER_BIG_ENDIAN
%else
%define byteorder	-DBYTE_ORDER_LITTLE_ENDIAN
%endif

./configure --force-libpcap
:>bytesex.h

%{__make} \
	CC="%{__cc}" \
	CCOPT="%{rpmcflags} %{byteorder}" \
	DEBUG=""

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install hping2 $RPM_BUILD_ROOT%{_sbindir}
install docs/hping2.8  $RPM_BUILD_ROOT%{_mandir}/man8

ln -sf hping2 $RPM_BUILD_ROOT%{_sbindir}/hping

rm -fR docs/CVS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING *BUGS README TODO docs/[A-Z]*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
