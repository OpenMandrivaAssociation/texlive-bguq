%global tl_name bguq
%global tl_revision 27401

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.4
Release:	%{tl_revision}.1
Summary:	Improved quantifier stroke for Begriffsschrift packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bguq
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bguq.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bguq.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bguq.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The font contains a single character: the Begriffsschrift quantifier (in
several sizes), as used to set the Begriffsschrift (concept notation) of
Frege. The font is not intended for end users; instead it is expected
that it will be used by other packages which implement the
Begriffsschrift. An (unofficial) modified version of Josh Parsons'
begriff is included as an example of implementation.

%prep
%setup -q -c -a1 -a2
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
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/fonts
%dir %{_datadir}/texmf-dist/fonts/map
%dir %{_datadir}/texmf-dist/fonts/source
%dir %{_datadir}/texmf-dist/fonts/tfm
%dir %{_datadir}/texmf-dist/fonts/type1
%dir %{_datadir}/texmf-dist/source/fonts
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/fonts/bguq
%dir %{_datadir}/texmf-dist/fonts/map/dvips
%dir %{_datadir}/texmf-dist/fonts/source/public
%dir %{_datadir}/texmf-dist/fonts/tfm/public
%dir %{_datadir}/texmf-dist/fonts/type1/public
%dir %{_datadir}/texmf-dist/source/fonts/bguq
%dir %{_datadir}/texmf-dist/tex/latex/bguq
%dir %{_datadir}/texmf-dist/fonts/map/dvips/bguq
%dir %{_datadir}/texmf-dist/fonts/source/public/bguq
%dir %{_datadir}/texmf-dist/fonts/tfm/public/bguq
%dir %{_datadir}/texmf-dist/fonts/type1/public/bguq
%doc %{_datadir}/texmf-dist/doc/fonts/bguq/INSTALL.txt
%doc %{_datadir}/texmf-dist/doc/fonts/bguq/Makefile
%doc %{_datadir}/texmf-dist/doc/fonts/bguq/README
%doc %{_datadir}/texmf-dist/doc/fonts/bguq/bguq-doc.pdf
%{_datadir}/texmf-dist/fonts/map/dvips/bguq/bguq.map
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq10t04.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq10t05.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq10t06.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq10t07.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq10t08.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq10t09.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq10t10.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq10t11.mf
%doc %{_datadir}/texmf-dist/fonts/source/public/bguq/bguq10t12.mf
%{_datadir}/texmf-dist/fonts/tfm/public/bguq/bguq10t04.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bguq/bguq10t05.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bguq/bguq10t06.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bguq/bguq10t07.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bguq/bguq10t08.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bguq/bguq10t09.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bguq/bguq10t10.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bguq/bguq10t11.tfm
%{_datadir}/texmf-dist/fonts/tfm/public/bguq/bguq10t12.tfm
%{_datadir}/texmf-dist/fonts/type1/public/bguq/bguq10t04.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bguq/bguq10t05.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bguq/bguq10t06.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bguq/bguq10t07.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bguq/bguq10t08.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bguq/bguq10t09.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bguq/bguq10t10.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bguq/bguq10t11.pfb
%{_datadir}/texmf-dist/fonts/type1/public/bguq/bguq10t12.pfb
%doc %{_datadir}/texmf-dist/source/fonts/bguq/bguq.dtx
%doc %{_datadir}/texmf-dist/source/fonts/bguq/bguq.ins
%{_datadir}/texmf-dist/tex/latex/bguq/Ubguq04.fd
%{_datadir}/texmf-dist/tex/latex/bguq/Ubguq05.fd
%{_datadir}/texmf-dist/tex/latex/bguq/Ubguq06.fd
%{_datadir}/texmf-dist/tex/latex/bguq/Ubguq07.fd
%{_datadir}/texmf-dist/tex/latex/bguq/Ubguq08.fd
%{_datadir}/texmf-dist/tex/latex/bguq/Ubguq09.fd
%{_datadir}/texmf-dist/tex/latex/bguq/Ubguq10.fd
%{_datadir}/texmf-dist/tex/latex/bguq/Ubguq11.fd
%{_datadir}/texmf-dist/tex/latex/bguq/Ubguq12.fd
%{_datadir}/texmf-dist/tex/latex/bguq/begriff-bguq.sty
%{_datadir}/texmf-dist/tex/latex/bguq/bguq.cfg
%{_datadir}/texmf-dist/tex/latex/bguq/bguq.sty
