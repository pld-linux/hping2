Summary:	A software to do TCP/IP stack auditing and much more
Name:		hping2
Version:	beta54
Release:	1
License:	GPL/BSD
Group:		Networking/Utilities
Group(pl):	Sieciowe/Narzêdzia
URL:		http://www.kyuzz.org/antirez/hping2.html
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-system-libpcap.patch
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hping2 is a network tool able to send custom ICMP/UDP/TCP
packets and to display target replies like ping do with
ICMP replies. hping2 handle fragmentation, arbitrary packet
body and size and can be used in order to transfer files
under supported protocols.

%prep
%setup -q
%patch -p1

%build
MANPATH="%{_mandir}" \
./configure --force-libpcap

%{__make} CCOPT="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install hping2 $RPM_BUILD_ROOT%{_sbindir}
install docs/hping2.8  $RPM_BUILD_ROOT%{_mandir}/man8

ln -sf hping2 $RPM_BUILD_ROOT%{_sbindir}/hping

gzip -9nf COPYING *BUGS NOTIFY README TODO docs/[A-Z]*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {COPYING,*BUGS,NOTIFY,README,TODO}.gz docs/[A-Z]*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
