#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : svgpart
Version  : 19.12.3
Release  : 17
URL      : https://download.kde.org/stable/release-service/19.12.3/src/svgpart-19.12.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/19.12.3/src/svgpart-19.12.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/19.12.3/src/svgpart-19.12.3.tar.xz.sig
Summary  : A KPart for viewing SVGs
Group    : Development/Tools
License  : GPL-2.0
Requires: svgpart-data = %{version}-%{release}
Requires: svgpart-lib = %{version}-%{release}
Requires: svgpart-license = %{version}-%{release}
Requires: svgpart-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : qtbase-dev mesa-dev

%description
No detailed description available

%package data
Summary: data components for the svgpart package.
Group: Data

%description data
data components for the svgpart package.


%package lib
Summary: lib components for the svgpart package.
Group: Libraries
Requires: svgpart-data = %{version}-%{release}
Requires: svgpart-license = %{version}-%{release}

%description lib
lib components for the svgpart package.


%package license
Summary: license components for the svgpart package.
Group: Default

%description license
license components for the svgpart package.


%package locales
Summary: locales components for the svgpart package.
Group: Default

%description locales
locales components for the svgpart package.


%prep
%setup -q -n svgpart-19.12.3
cd %{_builddir}/svgpart-19.12.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583528663
mkdir -p clr-build
pushd clr-build
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1583528663
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/svgpart
cp %{_builddir}/svgpart-19.12.3/COPYING %{buildroot}/usr/share/package-licenses/svgpart/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
pushd clr-build
%make_install
popd
%find_lang svgpart

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/svgpart.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt5/plugins/kf5/parts/svgpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/svgpart/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files locales -f svgpart.lang
%defattr(-,root,root,-)

