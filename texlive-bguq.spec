%global tl_name bguq
%global tl_revision 27401
%global tl_version 0.4

Name:		texlive-%{tl_name}
Epoch:		1
Version:	%{tl_version}
Release:	%{tl_revision}.1
Summary:	Improved quantifier stroke for Begriffsschrift packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/bguq
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bguq.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bguq.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bguq.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
The font contains a single character: the Begriffsschrift quantifier (in
several sizes), as used to set the Begriffsschrift (concept notation) of
Frege. The font is not intended for end users; instead it is expected
that it will be used by other packages which implement the
Begriffsschrift. An (unofficial) modified version of Josh Parsons'
begriff is included as an example of implementation.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from bguq:
Map bguq.map
TL_DROPIN_EOF
