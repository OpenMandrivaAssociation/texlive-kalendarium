Name:		texlive-kalendarium
Version:	48744
Release:	1
Summary:	Print dates according to the classical Latin calendar
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/kalendarium
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kalendarium.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kalendarium.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kalendarium.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
kalendarium is a LaTeX3 package that provides several macros
with which to print dates in classical Latin given days on the
Julian or Gregorian calendars, using the same syntax used by
ancient Roman authors. The format of these dates may be
customised either in the package options or on a per-command
basis; these options also allow for the generation of date
strings according to different eras of the Classical period.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/kalendarium
%{_texmfdistdir}/tex/latex/kalendarium
%doc %{_texmfdistdir}/doc/latex/kalendarium

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
