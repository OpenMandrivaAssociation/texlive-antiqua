Name:		texlive-antiqua
Version:	24266
Release:	2
Summary:	URW Antiqua condensed font, for use with TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/urw/antiqua
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/antiqua.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/antiqua.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The directory contains a copy of the Type 1 font "URW Antiqua
2051 Regular Condensed" released under the GPL by URW, with
supporting files for use with (La)TeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/urw/antiqua/uaqr8ac.afm
%{_texmfdistdir}/fonts/map/dvips/antiqua/uaq.map
%{_texmfdistdir}/fonts/map/vtex/antiqua/uaq.ali
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqr7tc.tfm
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqr8ac.tfm
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqr8cc.tfm
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqr8rc.tfm
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqr8tc.tfm
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqrc7tc.tfm
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqrc8tc.tfm
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqro7tc.tfm
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqro8cc.tfm
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqro8rc.tfm
%{_texmfdistdir}/fonts/tfm/urw/antiqua/uaqro8tc.tfm
%{_texmfdistdir}/fonts/type1/urw/antiqua/uaqr8ac.pfb
%{_texmfdistdir}/fonts/type1/urw/antiqua/uaqr8ac.pfm
%{_texmfdistdir}/fonts/vf/urw/antiqua/uaqr7tc.vf
%{_texmfdistdir}/fonts/vf/urw/antiqua/uaqr8cc.vf
%{_texmfdistdir}/fonts/vf/urw/antiqua/uaqr8tc.vf
%{_texmfdistdir}/fonts/vf/urw/antiqua/uaqrc7tc.vf
%{_texmfdistdir}/fonts/vf/urw/antiqua/uaqrc8tc.vf
%{_texmfdistdir}/fonts/vf/urw/antiqua/uaqro7tc.vf
%{_texmfdistdir}/fonts/vf/urw/antiqua/uaqro8cc.vf
%{_texmfdistdir}/fonts/vf/urw/antiqua/uaqro8tc.vf
%{_texmfdistdir}/tex/latex/antiqua/ot1uaq.fd
%{_texmfdistdir}/tex/latex/antiqua/t1uaq.fd
%{_texmfdistdir}/tex/latex/antiqua/ts1uaq.fd
%doc %{_texmfdistdir}/doc/fonts/antiqua/antiqua.txt
%doc %{_texmfdistdir}/doc/fonts/antiqua/uaqr8ac.afm.org

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
