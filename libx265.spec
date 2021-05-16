#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : libx265
Version  : 3.5
Release  : 21
URL      : file:///aot/build/clearlinux/packages/libx265/libx265-v3.5.tar.gz
Source0  : file:///aot/build/clearlinux/packages/libx265/libx265-v3.5.tar.gz
Summary  : H.265/HEVC video encoder
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : Z3-dev
BuildRequires : Z3-staticdev
BuildRequires : binutils-dev
BuildRequires : buildreq-cmake
BuildRequires : ccache
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : findutils
BuildRequires : gcc
BuildRequires : gcc-dev
BuildRequires : gcc-libs-math
BuildRequires : gcc-libstdc++32
BuildRequires : gcc-libubsan
BuildRequires : gcc-locale
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : glibc-staticdev
BuildRequires : libedit
BuildRequires : libedit-dev
BuildRequires : libffi-dev
BuildRequires : libffi-staticdev
BuildRequires : libgcc1
BuildRequires : libstdc++
BuildRequires : libxml2-dev
BuildRequires : libxml2-staticdev
BuildRequires : nasm-bin
BuildRequires : ncurses-dev
BuildRequires : python3-dev
BuildRequires : python3-staticdev
BuildRequires : xz-dev
BuildRequires : xz-staticdev
BuildRequires : yaml-cpp
BuildRequires : yaml-cpp-dev
BuildRequires : zlib-dev
BuildRequires : zlib-staticdev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
=================
x265 HEVC Encoder
=================
| **Read:** | Online `documentation <http://x265.readthedocs.org/en/master/>`_ | Developer `wiki <http://bitbucket.org/multicoreware/x265_git/wiki/>`_
| **Download:** | `releases <http://ftp.videolan.org/pub/videolan/x265/>`_
| **Interact:** | #x265 on freenode.irc.net | `x265-devel@videolan.org <http://mailman.videolan.org/listinfo/x265-devel>`_ | `Report an issue <https://bitbucket.org/multicoreware/x265/issues?status=new&status=open>`_

%prep
%setup -q -n libx265
cd %{_builddir}/libx265

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621152527
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
## altflags_pgo content
## pgo generate
export PGO_GEN="-fprofile-generate=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-update=atomic -fprofile-arcs -ftest-coverage --coverage -fprofile-partial-training"
export CFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FCFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export FFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export CXXFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -fvisibility-inlines-hidden -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
export LDFLAGS_GENERATE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -falign-functions=32 -flimit-function-alignment -fno-semantic-interposition -fno-stack-protector -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -mtls-dialect=gnu2 -fno-math-errno -fno-trapping-math -pipe -ffat-lto-objects -flto=16 -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread -Wl,--build-id=sha1 -fdevirtualize-at-ltrans -Wl,-z,now -Wl,-z,relro -Wl,-sort-common -fasynchronous-unwind-tables $PGO_GEN"
## pgo use
## -ffat-lto-objects -fno-PIE -fno-PIE -m64 -no-pie -fPIC -Wl,-z,max-page-size=0x1000 -fvisibility=hidden -flto-partition=none
## gcc: -feliminate-unused-debug-types -fipa-pta -flto=16 -Wno-error -Wp,-D_REENTRANT -fno-common
export PGO_USE="-fprofile-use=/var/tmp/pgo -fprofile-dir=/var/tmp/pgo -fprofile-abs-path -fprofile-correction -fprofile-partial-training"
export CFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FCFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export FFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export CXXFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -fvisibility-inlines-hidden -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc $PGO_USE"
export LDFLAGS_USE="-g -O3 --param=lto-max-streaming-parallelism=16 -march=native -mtune=native -fgraphite-identity -Wall -Wl,--as-needed -Wl,--build-id=sha1 -Wl,--enable-new-dtags -Wl,--hash-style=gnu -Wl,-O2 -Wl,-z,now -Wl,-z,relro -falign-functions=32 -flimit-function-alignment -fasynchronous-unwind-tables -fdevirtualize-at-ltrans -floop-nest-optimize -floop-block -fno-math-errno -fno-semantic-interposition -fno-stack-protector -fno-trapping-math -ftree-loop-distribute-patterns -ftree-loop-vectorize -ftree-vectorize -funroll-loops -fuse-ld=bfd -fuse-linker-plugin -malign-data=cacheline -feliminate-unused-debug-types -fipa-pta -flto=16 -fno-plt -mtls-dialect=gnu2 -Wl,-sort-common -Wno-error -Wp,-D_REENTRANT -pipe -ffat-lto-objects -fPIC -Wl,-z,max-page-size=0x1000 -fomit-frame-pointer -pthread -static-libstdc++ -static-libgcc -lpthread $PGO_USE"
#
export AR=/usr/bin/gcc-ar
export RANLIB=/usr/bin/gcc-ranlib
export NM=/usr/bin/gcc-nm
#
export MAKEFLAGS=%{?_smp_mflags}
#
%global _lto_cflags 1
#global _lto_cflags %{nil}
%global _disable_maintainer_mode 1
#%global _disable_maintainer_mode %{nil}
#
export CCACHE_DISABLE=true
export PATH="/usr/lib64/ccache/bin:$PATH"
export CCACHE_NOHASHDIR=true
export CCACHE_CPP2=true
export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,file_stat_matches,file_stat_matches_ctime,include_file_ctime,include_file_mtime,modules,system_headers,clang_index_store,file_macro
#export CCACHE_SLOPPINESS=modules,include_file_mtime,include_file_ctime,time_macros,pch_defines,file_stat_matches,clang_index_store,system_headers,locale
#export CCACHE_SLOPPINESS=pch_defines,time_macros,locale,clang_index_store,file_macro
export CCACHE_DIR=/var/tmp/ccache
export CCACHE_BASEDIR=/builddir/build/BUILD
#export CCACHE_LOGFILE=/var/tmp/ccache/cache.debug
#export CCACHE_DEBUG=true
#export CCACHE_NODIRECT=true
## altflags_pgo end
if [ ! -f statuspgo ]; then
echo PGO Phase 1
export CFLAGS="${CFLAGS_GENERATE}"
export CXXFLAGS="${CXXFLAGS_GENERATE}"
export FFLAGS="${FFLAGS_GENERATE}"
export FCFLAGS="${FCFLAGS_GENERATE}"
export LDFLAGS="${LDFLAGS_GENERATE}"
mkdir -p 8bit 10bit 12bit

cd 12bit
cmake ../../source -G "Unix Makefiles" -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64 -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_NM=/usr/bin/gcc-nm -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DLIB_INSTALL_DIR=lib64 -DNATIVE_BUILD:BOOL=ON -DSTATIC_LINK_CRT:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON -DENABLE_SHARED:BOOL=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_DOCS:BOOL=OFF -DENABLE_ASSEMBLY:BOOL=ON -DENABLE_NASM:BOOL=ON -DENABLE_PIC:BOOL=ON -DENABLE_LIBNUMA:BOOL=OFF -DENABLE_LIBNUMA:BOOL=OFF -DEXPORT_C_API:BOOL=OFF -DENABLE_CLI:BOOL=OFF -DMAIN12:BOOL=ON -DHIGH_BIT_DEPTH:BOOL=ON
make -j16 V=1 VERBOSE=1

cd ../10bit
cmake ../../source -G "Unix Makefiles" -DCMAKE_VERBOSE_MAKEFILE:BOOL:BOOL=ON -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64 -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_NM=/usr/bin/gcc-nm -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DLIB_INSTALL_DIR=lib64 -DNATIVE_BUILD:BOOL=ON -DSTATIC_LINK_CRT:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON -DENABLE_SHARED:BOOL=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_DOCS:BOOL=OFF -DENABLE_ASSEMBLY:BOOL=ON -DENABLE_NASM:BOOL=ON -DENABLE_PIC:BOOL=ON -DENABLE_LIBNUMA:BOOL=OFF -DEXPORT_C_API:BOOL=OFF -DENABLE_CLI:BOOL=OFF -DHIGH_BIT_DEPTH:BOOL=ON
make -j16 V=1 VERBOSE=1

cd ../8bit
cp -f ../10bit/libx265.a libx265_main10.a
cp -f ../12bit/libx265.a libx265_main12.a
cmake ../../source -G "Unix Makefiles" -DCMAKE_VERBOSE_MAKEFILE:BOOL:BOOL=ON -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64 -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_NM=/usr/bin/gcc-nm -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DLIB_INSTALL_DIR=lib64 -DNATIVE_BUILD:BOOL=ON -DSTATIC_LINK_CRT:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON -DENABLE_SHARED:BOOL=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_DOCS:BOOL=OFF -DENABLE_ASSEMBLY:BOOL=ON -DENABLE_NASM:BOOL=ON -DENABLE_PIC:BOOL=ON -DENABLE_LIBNUMA:BOOL=OFF -DHIGH_BIT_DEPTH:BOOL=ON -DENABLE_HDR10_PLUS:BOOL=ON -DENABLE_TESTS:BOOL=ON -DENABLE_CLI:BOOL=ON -DEXTRA_LIB="x265_main10.a;x265_main12.a" -DEXTRA_LINK_FLAGS="-L. -L/usr/lib64" -DLINKED_10BIT:BOOL=ON -DLINKED_12BIT:BOOL=ON
make -j16 V=1 VERBOSE=1

# rename the 8bit library, then combine all three into libx265.a
mv libx265.a libx265_main.a
# On Linux, we use GNU ar to combine the static libraries together
gcc-ar -M <<EOF
CREATE libx265.a
ADDLIB libx265_main.a
ADDLIB libx265_main10.a
ADDLIB libx265_main12.a
SAVE
END
EOF
#
echo "PGO..."

export LD_LIBRARY_PATH=".:$LD_LIBRARY_PATH"
./x265 --input /opt/fprofile/harry.y4m --crf 20 --output /dev/null
./x265 --input /opt/fprofile/eyes.y4m --crf 20 --output /dev/null
./x265 --input /opt/fprofile/allied.y4m --crf 20 --output /dev/null
./x265 --input /opt/fprofile/harry2.y4m --crf 20 --output /dev/null
cd ..
find . -type f,l -not -name '*.gcno' -not -name 'statuspgo*' -delete -print
echo USED > statuspgo
fi
if [ -f statuspgo ]; then
echo PGO Phase 2
export CFLAGS="${CFLAGS_USE}"
export CXXFLAGS="${CXXFLAGS_USE}"
export FFLAGS="${FFLAGS_USE}"
export FCFLAGS="${FCFLAGS_USE}"
export LDFLAGS="${LDFLAGS_USE}"
mkdir -p 8bit 10bit 12bit

cd 12bit
cmake ../../source -G "Unix Makefiles" -DCMAKE_VERBOSE_MAKEFILE:BOOL=ON -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64 -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_NM=/usr/bin/gcc-nm -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DLIB_INSTALL_DIR=lib64 -DNATIVE_BUILD:BOOL=ON -DSTATIC_LINK_CRT:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON -DENABLE_SHARED:BOOL=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_DOCS:BOOL=OFF -DENABLE_ASSEMBLY:BOOL=ON -DENABLE_NASM:BOOL=ON -DENABLE_PIC:BOOL=ON -DENABLE_LIBNUMA:BOOL=OFF -DENABLE_LIBNUMA:BOOL=OFF -DEXPORT_C_API:BOOL=OFF -DENABLE_CLI:BOOL=OFF -DMAIN12:BOOL=ON -DHIGH_BIT_DEPTH:BOOL=ON
make -j16 V=1 VERBOSE=1

cd ../10bit
cmake ../../source -G "Unix Makefiles" -DCMAKE_VERBOSE_MAKEFILE:BOOL:BOOL=ON -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64 -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_NM=/usr/bin/gcc-nm -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DLIB_INSTALL_DIR=lib64 -DNATIVE_BUILD:BOOL=ON -DSTATIC_LINK_CRT:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON -DENABLE_SHARED:BOOL=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_DOCS:BOOL=OFF -DENABLE_ASSEMBLY:BOOL=ON -DENABLE_NASM:BOOL=ON -DENABLE_PIC:BOOL=ON -DENABLE_LIBNUMA:BOOL=OFF -DEXPORT_C_API:BOOL=OFF -DENABLE_CLI:BOOL=OFF -DHIGH_BIT_DEPTH:BOOL=ON
make -j16 V=1 VERBOSE=1

cd ../8bit
cp -f ../10bit/libx265.a libx265_main10.a
cp -f ../12bit/libx265.a libx265_main12.a
cmake ../../source -G "Unix Makefiles" -DCMAKE_VERBOSE_MAKEFILE:BOOL:BOOL=ON -DCMAKE_INSTALL_PREFIX=/usr -DLIB_SUFFIX=64 -DCMAKE_AR=/usr/bin/gcc-ar -DCMAKE_NM=/usr/bin/gcc-nm -DCMAKE_RANLIB=/usr/bin/gcc-ranlib -DLIB_INSTALL_DIR=lib64 -DNATIVE_BUILD:BOOL=ON -DSTATIC_LINK_CRT:BOOL=ON -DBUILD_STATIC_LIBS:BOOL=ON -DENABLE_SHARED:BOOL=ON -DCMAKE_BUILD_TYPE=Release -DENABLE_DOCS:BOOL=OFF -DENABLE_ASSEMBLY:BOOL=ON -DENABLE_NASM:BOOL=ON -DENABLE_PIC:BOOL=ON -DENABLE_LIBNUMA:BOOL=OFF -DHIGH_BIT_DEPTH:BOOL=ON -DENABLE_HDR10_PLUS:BOOL=ON -DENABLE_TESTS:BOOL=ON -DENABLE_CLI:BOOL=ON -DEXTRA_LIB="x265_main10.a;x265_main12.a" -DEXTRA_LINK_FLAGS="-L. -L/usr/lib64" -DLINKED_10BIT:BOOL=ON -DLINKED_12BIT:BOOL=ON
make -j16 V=1 VERBOSE=1

# rename the 8bit library, then combine all three into libx265.a
mv libx265.a libx265_main.a
# On Linux, we use GNU ar to combine the static libraries together
gcc-ar -M <<EOF
CREATE libx265.a
ADDLIB libx265_main.a
ADDLIB libx265_main10.a
ADDLIB libx265_main12.a
SAVE
END
EOF
#
echo "PGO..."
fi
popd

%install
export SOURCE_DATE_EPOCH=1621152527
rm -rf %{buildroot}
## install_macro start
pushd 8bit
%make_install
popd
## install_macro end

%files
%defattr(-,root,root,-)
