%global tl_name antiqua
%global tl_revision 24266
%global tl_version 001.003

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	URW Antiqua condensed font, for use with TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/urw/antiqua
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antiqua.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/antiqua.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The package contains a copy of the Type 1 font "URW Antiqua 2051 Regular
Condensed" released under the GPL by URW, with supporting files for use
with (La)TeX.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from antiqua:
Map uaq.map
TL_DROPIN_EOF
