%global tl_name antiqua
%global tl_revision 24266

Name:		texlive-%{tl_name}
Epoch:		1
Version:	001.003
Release:	%{tl_revision}.1
Summary:	URW Antiqua condensed font, for use with TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/urw/antiqua
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antiqua.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antiqua.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains a copy of the Type 1 font "URW Antiqua 2051 Regular
Condensed" released under the GPL by URW, with supporting files for use
with (La)TeX.

