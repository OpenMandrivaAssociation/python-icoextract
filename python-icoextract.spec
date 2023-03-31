Name:           python-icoextract
Version:        0.1.4
Release:        2
Summary:        Extract icons from Windows PE files (.exe/.dll)
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/jlu5/icoextract
Source:         https://github.com/jlu5/icoextract/archive/%{version}/icoextract-%{version}.tar.gz

BuildRequires:  python3dist(pefile)
BuildRequires:  python3dist(pillow)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(wheel)
BuildRequires:  imagemagick
BuildRequires:  cmake

Requires:  python3dist(pefile)
Requires:  python3dist(pillow)

BuildArch:      noarch

%description
icoextract is an icon extractor for Windows PE files (.exe/.dll), written in
Python. It also includes a thumbnailer script (exe-thumbnailer) for Linux
desktops.

%prep
%autosetup -n icoextract-%{version} -p1

find . -name \*.py -exec sed -i -e '1{\@^#!%{_bindir}/env python@d}' '{}' \;

%build
%py_build

%install
%py_install

mkdir -p %{buildroot}%{_datadir}/thumbnailers/
cp exe-thumbnailer.thumbnailer %{buildroot}%{_datadir}/thumbnailers/

%files
%{_bindir}/exe-thumbnailer
%{_bindir}/icoextract
%{_bindir}/icolist
%{_datadir}/thumbnailers/exe-thumbnailer.thumbnailer
%{python_sitelib}/icoextract-%{version}-py*.*.egg-info
%{python_sitelib}/icoextract/
