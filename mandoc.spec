Summary:	Man page compiler toolset
Summary(pl.UTF-8):	Zestaw kompilatorów stron podręcznika (man)
Name:		mandoc
Version:	1.14.6
Release:	1
License:	ISC
Group:		Development/Tools
Source0:	https://mandoc.bsd.lv/snapshots/%{name}-%{version}.tar.gz
# Source0-md5:	f0adf24e8fdef5f3e332191f653e422a
URL:		https://mandoc.bsd.lv/
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The mandoc manpage compiler toolset (formerly called "mdocml")
is a suite of tools compiling mdoc, the roff macro language of choice
for BSD manual pages, and man, the predominant historical language for
UNIX manuals.

%description -l pl.UTF-8
Zestaw kompilatorów stron podręcznika mandoc (wcześniej znany jako
"mdocml") to zestaw narzędzi do kompilowania mdoc (języka makr roffa,
wybranego do stron podręcznika BSD) oraz man (głównego języka
historycznego podręczników uniksowych).

%package man
Summary:	Manual page viewer from mandoc project
Summary(pl.UTF-8):	Przeglądarka stron podręcznika z projektu mandoc
Group:		Documentation
Obsoletes:	man < 1.7
Obsoletes:	man-config < 1.7
Obsoletes:	man-db
Obsoletes:	man-whatis < 1.7

%description man
Manual page viewer from mandoc project.

%description man -l pl.UTF-8
Przeglądarka stron podręcznika z projektu mandoc.

%package devel
Summary:	Header files and static libmandoc library
Summary(pl.UTF-8):	Pliki nagłówkowe i statyczna biblioteka libmandoc
Group:		Development/Libraries

%description devel
Header files and static libmandoc library.

%description devel -l pl.UTF-8
Pliki nagłówkowe i statyczna biblioteka libmandoc.

%prep
%setup -q

%build
# non-autoconf configure
cat >configure.local <<EOF
CC="%{__cc}"
HAVE_WCHAR=1
UTF8_LOCALE=C.UTF-8
MANPATH_DEFAULT="/usr/share/man:/usr/local/share/man"
MANPATH_DEFAULT="/usr/share/man"
PREFIX="%{_prefix}"
MANDIR="%{_mandir}"
MANM_MAN="mandoc_man"
MANM_MDOC="mandoc_mdoc"
MANM_ROFF="mandoc_roff"
MANM_EQN="mandoc_eqn"
MANM_TBL="mandoc_tbl"
BINM_SOELIM="msoelim"
LN="ln -sf"
LDFLAGS="%{rpmldflags}"
INSTALL_PROGRAM="install -m755"
INSTALL_LIB="install -m644"
INSTALL_MAN="install -m644"
INSTALL_DATA="install -m644"
INSTALL_LIBMANDOC=1
LIBDIR="%{_libdir}"
CFLAGS="%{rpmcflags} -W -Wall -Wmissing-prototypes -Wstrict-prototypes -Wwrite-strings -Wno-unused-parameter"
EOF
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS TODO
%attr(755,root,root) %{_bindir}/demandoc
%attr(755,root,root) %{_bindir}/mandoc
%attr(755,root,root) %{_bindir}/msoelim
%{_mandir}/man1/demandoc.1*
%{_mandir}/man1/mandoc.1*
%{_mandir}/man1/msoelim.1*
%{_mandir}/man7/mandoc_eqn.7*
%{_mandir}/man7/mandoc_man.7*
%{_mandir}/man7/mandoc_char.7*
%{_mandir}/man7/mandoc_mdoc.7*
%{_mandir}/man7/mandoc_roff.7*
%{_mandir}/man7/mandoc_tbl.7*

%files man
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apropos
%attr(755,root,root) %{_bindir}/man
%attr(755,root,root) %{_bindir}/whatis
%attr(755,root,root) %{_sbindir}/makewhatis
%{_mandir}/man1/apropos.1*
%{_mandir}/man1/man.1*
%{_mandir}/man1/whatis.1*
%{_mandir}/man5/man.conf.5*
%{_mandir}/man5/mandoc.db.5*
%{_mandir}/man8/makewhatis.8*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libmandoc.a
%{_includedir}/mandoc
%{_mandir}/man3/mandoc.3*
%{_mandir}/man3/mandoc_escape.3*
%{_mandir}/man3/mandoc_malloc.3*
%{_mandir}/man3/mansearch.3*
%{_mandir}/man3/mchars_alloc.3*
%{_mandir}/man3/tbl.3*
