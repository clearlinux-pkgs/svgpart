#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : svgpart
Version  : 23.04.3
Release  : 54
URL      : https://download.kde.org/stable/release-service/23.04.3/src/svgpart-23.04.3.tar.xz
Source0  : https://download.kde.org/stable/release-service/23.04.3/src/svgpart-23.04.3.tar.xz
Source1  : https://download.kde.org/stable/release-service/23.04.3/src/svgpart-23.04.3.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0
Requires: svgpart-data = %{version}-%{release}
Requires: svgpart-lib = %{version}-%{release}
Requires: svgpart-license = %{version}-%{release}
Requires: svgpart-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n svgpart-23.04.3
cd %{_builddir}/svgpart-23.04.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1688833474
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FCFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export FFLAGS="$FFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -O3 -Wl,-z,x86-64-v3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd -march=x86-64-v3 "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1688833474
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/svgpart
cp %{_builddir}/svgpart-%{version}/CMakePresets.json.license %{buildroot}/usr/share/package-licenses/svgpart/29fb05b49e12a380545499938c4879440bd8851e || :
cp %{_builddir}/svgpart-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/svgpart/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build
%make_install
popd
%find_lang svgpart
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/kservices5/svgpart.desktop
/usr/share/metainfo/org.kde.svgpart.metainfo.xml

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/qt5/plugins/kf5/parts/svgpart.so
/usr/lib64/qt5/plugins/kf5/parts/svgpart.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/svgpart/29fb05b49e12a380545499938c4879440bd8851e
/usr/share/package-licenses/svgpart/e712eadfab0d2357c0f50f599ef35ee0d87534cb

%files locales -f svgpart.lang
%defattr(-,root,root,-)

