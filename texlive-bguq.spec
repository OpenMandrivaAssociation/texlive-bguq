# revision 27140
# category Package
# catalog-ctan /fonts/bguq
# catalog-date 2012-07-24 10:27:04 +0200
# catalog-license lppl
# catalog-version 0.3
Name:		texlive-bguq
Version:	0.3
Release:	1
Summary:	Improved quantifier stroke for Begriffsschrift packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/bguq
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bguq.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bguq.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bguq.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The font contains a single character: the Begriffsschrift
quantifier (in several sizes), as used to set the
Begriffsschrift (concept notation) of Frege. The font is not
intended for end users; instead it is expected that it will be
used by other packages which implement the Begriffsschrift. An
(unofficial) modified version of Josh Parsons' begriff is
included as an example of implementation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/map/dvips/bguq/bguq.map
%{_texmfdistdir}/fonts/source/public/bguq/bguq.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t04.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t05.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t06.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t07.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t08.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t09.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t10.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t11.mf
%{_texmfdistdir}/fonts/source/public/bguq/bguq10t12.mf
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t04.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t05.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t06.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t07.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t08.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t09.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t10.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t11.tfm
%{_texmfdistdir}/fonts/tfm/public/bguq/bguq10t12.tfm
%{_texmfdistdir}/fonts/type1/public/bguq/bguq10t04.pfb
%{_texmfdistdir}/fonts/type1/public/bguq/bguq10t05.pfb
%{_texmfdistdir}/fonts/type1/public/bguq/bguq10t06.pfb
%{_texmfdistdir}/fonts/type1/public/bguq/bguq10t07.pfb
%{_texmfdistdir}/fonts/type1/public/bguq/bguq10t08.pfb
%{_texmfdistdir}/fonts/type1/public/bguq/bguq10t09.pfb
%{_texmfdistdir}/fonts/type1/public/bguq/bguq10t10.pfb
%{_texmfdistdir}/fonts/type1/public/bguq/bguq10t11.pfb
%{_texmfdistdir}/fonts/type1/public/bguq/bguq10t12.pfb
%{_texmfdistdir}/tex/latex/bguq/Ubguq04.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq05.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq06.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq07.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq08.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq09.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq10.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq11.fd
%{_texmfdistdir}/tex/latex/bguq/Ubguq12.fd
%{_texmfdistdir}/tex/latex/bguq/begriff-bguq.sty
%{_texmfdistdir}/tex/latex/bguq/bguq.cfg
%{_texmfdistdir}/tex/latex/bguq/bguq.sty
%doc %{_texmfdistdir}/doc/fonts/bguq/INSTALL.txt
%doc %{_texmfdistdir}/doc/fonts/bguq/Makefile
%doc %{_texmfdistdir}/doc/fonts/bguq/README.txt
%doc %{_texmfdistdir}/doc/fonts/bguq/bguq-doc.pdf
#- source
%doc %{_texmfdistdir}/source/fonts/bguq/bguq.dtx
%doc %{_texmfdistdir}/source/fonts/bguq/bguq.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc source %{buildroot}%{_texmfdistdir}
