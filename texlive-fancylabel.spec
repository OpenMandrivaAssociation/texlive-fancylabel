Name:		texlive-fancylabel
Version:	46736
Release:	1
Summary:	Complex labelling with LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fancylabel
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancylabel.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancylabel.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fancylabel.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a complex labelling scheme. It is designed
to support the needs of the author's chemschemex package

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/fancylabel
%{_texmfdistdir}/tex/latex/fancylabel
%doc %{_texmfdistdir}/doc/latex/fancylabel

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
