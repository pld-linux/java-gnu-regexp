Summary:	Regular Expressions for Java
Summary(pl):	Wyra¿enia regularne dla jêzyka Java
Name:		gnu.regexp
Version:	1.1.4
Release:	1
Group:		Development/Languages/Java
Group(de):	Entwicklung/Sprachen/Java
Group(pl):	Programowanie/Jêzyki/Java
Url:		http://www.cacas.org/java/gnu/regexp
Source0:	ftp://ftp.tralfamadore.com/pub/java/%{name}-%{version}.tar.gz
License:	LGPL
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_javaclassdir	%{_libdir}/java/

%description
The gnu.regexp package is a pure-Java implementation of a traditional
(non-POSIX) NFA regular expression engine. Its syntax can emulate many
popular development tools, including awk, sed, emacs, perl and grep.

%description -l pl
Pakiet zawiera implementacjê tradycyjnych wyra¿eñ regularnych.
Sk³adnia tej implementacji emuluje wiele popularnych tego typu
narzêdzi, m.in.: awk, sed-a emacs-a, perl-a czy te¿ grep-a.

%prep
%setup -q

%build
cd src
%{__make} JAVAC=javac

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_javaclassdir}

install lib/gnu-regexp-%{version}.jar $RPM_BUILD_ROOT%{_javaclassdir}/gnu-regexp.jar

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_javaclassdir}/gnu-regexp.jar
