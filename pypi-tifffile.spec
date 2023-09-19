#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-tifffile
Version  : 2023.9.18
Release  : 58
URL      : https://files.pythonhosted.org/packages/17/9a/bab709cdd3ad445c8cdadf96fe58c5fbb883ee0ec3423ebc1c81e646c7ef/tifffile-2023.9.18.tar.gz
Source0  : https://files.pythonhosted.org/packages/17/9a/bab709cdd3ad445c8cdadf96fe58c5fbb883ee0ec3423ebc1c81e646c7ef/tifffile-2023.9.18.tar.gz
Summary  : Read and write TIFF files
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-tifffile-bin = %{version}-%{release}
Requires: pypi-tifffile-license = %{version}-%{release}
Requires: pypi-tifffile-python = %{version}-%{release}
Requires: pypi-tifffile-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(numpy)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Read and write TIFF files
=========================
Tifffile is a Python library to

%package bin
Summary: bin components for the pypi-tifffile package.
Group: Binaries
Requires: pypi-tifffile-license = %{version}-%{release}

%description bin
bin components for the pypi-tifffile package.


%package license
Summary: license components for the pypi-tifffile package.
Group: Default

%description license
license components for the pypi-tifffile package.


%package python
Summary: python components for the pypi-tifffile package.
Group: Default
Requires: pypi-tifffile-python3 = %{version}-%{release}

%description python
python components for the pypi-tifffile package.


%package python3
Summary: python3 components for the pypi-tifffile package.
Group: Default
Requires: python3-core
Provides: pypi(tifffile)
Requires: pypi(numpy)

%description python3
python3 components for the pypi-tifffile package.


%prep
%setup -q -n tifffile-2023.9.18
cd %{_builddir}/tifffile-2023.9.18
pushd ..
cp -a tifffile-2023.9.18 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695141959
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-tifffile
cp %{_builddir}/tifffile-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-tifffile/9cb65cbd9f0e99a02fcbbda3d3d7e93bbd4fad93 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lsm2bin
/usr/bin/tiff2fsspec
/usr/bin/tiffcomment
/usr/bin/tifffile

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-tifffile/9cb65cbd9f0e99a02fcbbda3d3d7e93bbd4fad93

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
