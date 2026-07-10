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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package contains a copy of the Type 1 font "URW Antiqua 2051 Regular
Condensed" released under the GPL by URW, with supporting files for use
with (La)TeX.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/fonts
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/afm
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/fonts/vf
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/antiqua
%dir %{_datadir}/texmf-dist/fonts/afm/urw
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/map/vtex
%dir %{_datadir}/texmf-dist/fonts/tfm/urw
%dir %{_datadir}/texmf-dist/fonts/type1/urw
%dir %{_datadir}/texmf-dist/fonts/vf/urw
%dir %{_datadir}/texmf-dist/tex/latex/antiqua
%dir %{_datadir}/texmf-dist/fonts/afm/urw/antiqua
%dir %{_datadir}/texmf-dist/fonts/map/dvips/antiqua
%dir %{_datadir}/texmf-dist/fonts/map/vtex/antiqua
%dir %{_datadir}/texmf-dist/fonts/tfm/urw/antiqua
%dir %{_datadir}/texmf-dist/fonts/type1/urw/antiqua
%dir %{_datadir}/texmf-dist/fonts/vf/urw/antiqua
%doc %{_datadir}/texmf-dist/doc/fonts/antiqua/antiqua.txt
%doc %{_datadir}/texmf-dist/doc/fonts/antiqua/uaqr8ac.afm.org
%{_datadir}/texmf-dist/fonts/afm/urw/antiqua/uaqr8ac.afm
%{_datadir}/texmf-dist/fonts/map/dvips/antiqua/uaq.map
%{_datadir}/texmf-dist/fonts/map/vtex/antiqua/uaq.ali
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqr7tc.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqr8ac.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqr8cc.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqr8rc.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqr8tc.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqrc7tc.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqrc8tc.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqro7tc.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqro8cc.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqro8rc.tfm
%{_datadir}/texmf-dist/fonts/tfm/urw/antiqua/uaqro8tc.tfm
%{_datadir}/texmf-dist/fonts/type1/urw/antiqua/uaqr8ac.pfb
%{_datadir}/texmf-dist/fonts/type1/urw/antiqua/uaqr8ac.pfm
%{_datadir}/texmf-dist/fonts/vf/urw/antiqua/uaqr7tc.vf
%{_datadir}/texmf-dist/fonts/vf/urw/antiqua/uaqr8cc.vf
%{_datadir}/texmf-dist/fonts/vf/urw/antiqua/uaqr8tc.vf
%{_datadir}/texmf-dist/fonts/vf/urw/antiqua/uaqrc7tc.vf
%{_datadir}/texmf-dist/fonts/vf/urw/antiqua/uaqrc8tc.vf
%{_datadir}/texmf-dist/fonts/vf/urw/antiqua/uaqro7tc.vf
%{_datadir}/texmf-dist/fonts/vf/urw/antiqua/uaqro8cc.vf
%{_datadir}/texmf-dist/fonts/vf/urw/antiqua/uaqro8tc.vf
%{_datadir}/texmf-dist/tex/latex/antiqua/ot1uaq.fd
%{_datadir}/texmf-dist/tex/latex/antiqua/t1uaq.fd
%{_datadir}/texmf-dist/tex/latex/antiqua/ts1uaq.fd
