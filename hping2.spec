Summary:	A software to do TCP/IP stack auditing and much more
Summary(pl):	Oprogramowanie do audytu stosu TCP/IP
Name:		hping2
Version:	2.0.0
Release:	3
License:	GPL/BSD
Group:		Networking/Utilities
Source0:	http://www.hping.org/%{name}.0.0-rc2.tar.gz
URL:		http://www.hping.org/
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hping2 is a network tool able to send custom ICMP/UDP/TCP packets and
to display target replies like ping do with ICMP replies. hping2
handle fragmentation, arbitrary packet body and size and can be used
in order to transfer files under supported protocols.

%description -l pl
hping2 to narz�dzie sieciowe do wysy�ania w�asnych pakiet�w
ICMP/UDP/TCP i wy�wietlania odpowiedzi, podobnie jak robi to ping z
odpowiedziami ICMP. hping2 obs�uguje fragmentacj�, dowolne zawarto�ci
i rozmiary pakiet�w i mo�e by� u�ywany do przesy�ania plik�w przez
obs�ugiwane protoko�y.

%prep
%setup -q -n hping2-rc2

%build
MANPATH="%{_mandir}" \
./configure --force-libpcap

%{__make} \
	CC="%{__cc}" \
	CCOPT="%{rpmcflags}"

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
