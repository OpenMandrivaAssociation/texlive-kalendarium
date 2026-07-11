%global tl_name kalendarium
%global tl_revision 48744

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Print dates according to the classical Latin calendar
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kalendarium
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kalendarium.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kalendarium.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/kalendarium.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
kalendarium is a LaTeX3 package that provides several macros with which
to print dates in classical Latin given days on the Julian or Gregorian
calendars, using the same syntax used by ancient Roman authors. The
format of these dates may be customised either in the package options or
on a per-command basis; these options also allow for the generation of
date strings according to different eras of the Classical period.

