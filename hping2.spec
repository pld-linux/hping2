Summary:	A software to do TCP/IP stack auditing and much more
Summary(pl):	Oprogramowanie do audytu stosu TCP/IP
Name:		hping2
Version:	2.0.0
Release:	2
License:	GPL/BSD
Group:		Networking/Utilities
Group(de):	Netzwerkwesen/Werkzeuge
Group(pl):	Sieciowe/Narzêdzia
URL:		http://www.hping.org/	
Source0:	http://www.hping.org/hping2.0.0-rc1.tar.gz
Patch0:		%{name}-system-libpcap.patch
BuildRequires:	libpcap-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hping2 is a network tool able to send custom ICMP/UDP/TCP packets and
to display target replies like ping do with ICMP replies. hping2
handle fragmentation, arbitrary packet body and size and can be used
in order to transfer files under supported protocols.

%prep
%setup -q -n hping2
#%patch -p1

%build
MANPATH="%{_mandir}" \
./configure --force-libpcap

%{__make} CCOPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install hping2 $RPM_BUILD_ROOT%{_sbindir}
install docs/hping2.8  $RPM_BUILD_ROOT%{_mandir}/man8

ln -sf hping2 $RPM_BUILD_ROOT%{_sbindir}/hping

rm -fR docs/CVS
gzip -9nf COPYING *BUGS README TODO docs/[A-Z]*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {COPYING,*BUGS,README,TODO}.gz docs/[A-Z]*
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
