Summary:	Regular Expressions for Java
Summary(pl.UTF-8):	Wyrażenia regularne dla języka Java
Name:		gnu.regexp
Version:	1.1.4
Release:	1
License:	LGPL
Group:		Development/Languages/Java
Source0:	ftp://ftp.tralfamadore.com/pub/java/%{name}-%{version}.tar.gz
# Source0-md5:	4b5a3722f1d814ee30591ad21b519d28
URL:		http://www.cacas.org/java/gnu/regexp/
BuildRequires:	jdk
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java

%description
The gnu.regexp package is a pure-Java implementation of a traditional
(non-POSIX) NFA regular expression engine. Its syntax can emulate many
popular development tools, including awk, sed, emacs, perl and grep.

%description -l pl.UTF-8
Pakiet zawiera implementację tradycyjnych wyrażeń regularnych.
Składnia tej implementacji emuluje wiele popularnych tego typu
narzędzi, m.in.: awk, seda, emacsa, Perla oraz grepa.

%prep
%setup -q

%build
cd src
%{__make} JAVAC=javac

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javaclassdir}

install lib/gnu-regexp-%{version}.jar $RPM_BUILD_ROOT%{_javaclassdir}/gnu-regexp.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{_javaclassdir}/gnu-regexp.jar
