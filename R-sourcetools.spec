#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sourcetools
Version  : 0.1.7
Release  : 47
URL      : https://cran.r-project.org/src/contrib/sourcetools_0.1.7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sourcetools_0.1.7.tar.gz
Summary  : Tools for Reading, Tokenizing and Parsing R Code
Group    : Development/Tools
License  : MIT
Requires: R-sourcetools-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
'sourcetools' package provides both an R and C++ interface for the tokenization
    of R code, and helpers for interacting with the tokenized representation of R
    code.

%package lib
Summary: lib components for the R-sourcetools package.
Group: Libraries

%description lib
lib components for the R-sourcetools package.


%prep
%setup -q -c -n sourcetools
cd %{_builddir}/sourcetools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589511516

%install
export SOURCE_DATE_EPOCH=1589511516
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sourcetools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sourcetools
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sourcetools
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc sourcetools || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/sourcetools/DESCRIPTION
/usr/lib64/R/library/sourcetools/INDEX
/usr/lib64/R/library/sourcetools/LICENSE
/usr/lib64/R/library/sourcetools/Meta/Rd.rds
/usr/lib64/R/library/sourcetools/Meta/features.rds
/usr/lib64/R/library/sourcetools/Meta/hsearch.rds
/usr/lib64/R/library/sourcetools/Meta/links.rds
/usr/lib64/R/library/sourcetools/Meta/nsInfo.rds
/usr/lib64/R/library/sourcetools/Meta/package.rds
/usr/lib64/R/library/sourcetools/NAMESPACE
/usr/lib64/R/library/sourcetools/NEWS.md
/usr/lib64/R/library/sourcetools/R/sourcetools
/usr/lib64/R/library/sourcetools/R/sourcetools.rdb
/usr/lib64/R/library/sourcetools/R/sourcetools.rdx
/usr/lib64/R/library/sourcetools/help/AnIndex
/usr/lib64/R/library/sourcetools/help/aliases.rds
/usr/lib64/R/library/sourcetools/help/paths.rds
/usr/lib64/R/library/sourcetools/help/sourcetools.rdb
/usr/lib64/R/library/sourcetools/help/sourcetools.rdx
/usr/lib64/R/library/sourcetools/html/00Index.html
/usr/lib64/R/library/sourcetools/html/R.css
/usr/lib64/R/library/sourcetools/include/sourcetools.h
/usr/lib64/R/library/sourcetools/include/sourcetools/collection/Position.h
/usr/lib64/R/library/sourcetools/include/sourcetools/collection/Range.h
/usr/lib64/R/library/sourcetools/include/sourcetools/collection/collection.h
/usr/lib64/R/library/sourcetools/include/sourcetools/core/core.h
/usr/lib64/R/library/sourcetools/include/sourcetools/core/macros.h
/usr/lib64/R/library/sourcetools/include/sourcetools/core/util.h
/usr/lib64/R/library/sourcetools/include/sourcetools/cursor/TextCursor.h
/usr/lib64/R/library/sourcetools/include/sourcetools/cursor/TokenCursor.h
/usr/lib64/R/library/sourcetools/include/sourcetools/cursor/cursor.h
/usr/lib64/R/library/sourcetools/include/sourcetools/multibyte/multibyte.h
/usr/lib64/R/library/sourcetools/include/sourcetools/platform/platform.h
/usr/lib64/R/library/sourcetools/include/sourcetools/r/RCallRecurser.h
/usr/lib64/R/library/sourcetools/include/sourcetools/r/RConverter.h
/usr/lib64/R/library/sourcetools/include/sourcetools/r/RFunctions.h
/usr/lib64/R/library/sourcetools/include/sourcetools/r/RHeaders.h
/usr/lib64/R/library/sourcetools/include/sourcetools/r/RNonStandardEvaluation.h
/usr/lib64/R/library/sourcetools/include/sourcetools/r/RUtils.h
/usr/lib64/R/library/sourcetools/include/sourcetools/r/r.h
/usr/lib64/R/library/sourcetools/include/sourcetools/read/MemoryMappedReader.h
/usr/lib64/R/library/sourcetools/include/sourcetools/read/posix/FileConnection.h
/usr/lib64/R/library/sourcetools/include/sourcetools/read/posix/MemoryMappedConnection.h
/usr/lib64/R/library/sourcetools/include/sourcetools/read/read.h
/usr/lib64/R/library/sourcetools/include/sourcetools/read/windows/FileConnection.h
/usr/lib64/R/library/sourcetools/include/sourcetools/read/windows/MemoryMappedConnection.h
/usr/lib64/R/library/sourcetools/include/sourcetools/tests/testthat.h
/usr/lib64/R/library/sourcetools/include/sourcetools/tokenization/Registration.h
/usr/lib64/R/library/sourcetools/include/sourcetools/tokenization/Token.h
/usr/lib64/R/library/sourcetools/include/sourcetools/tokenization/Tokenizer.h
/usr/lib64/R/library/sourcetools/include/sourcetools/tokenization/tokenization.h
/usr/lib64/R/library/sourcetools/include/sourcetools/utf8/utf8.h
/usr/lib64/R/library/sourcetools/tests/testthat.R
/usr/lib64/R/library/sourcetools/tests/testthat/helper-utf8.R
/usr/lib64/R/library/sourcetools/tests/testthat/test-read.R
/usr/lib64/R/library/sourcetools/tests/testthat/test-tokenize.R

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sourcetools/libs/sourcetools.so
