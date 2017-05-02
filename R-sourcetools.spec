#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-sourcetools
Version  : 0.1.6
Release  : 9
URL      : https://cran.r-project.org/src/contrib/sourcetools_0.1.6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/sourcetools_0.1.6.tar.gz
Summary  : Tools for Reading, Tokenizing and Parsing R Code
Group    : Development/Tools
License  : MIT
Requires: R-sourcetools-lib
BuildRequires : clr-R-helpers

%description
[![Travis-CI Build Status](https://travis-ci.org/kevinushey/sourcetools.svg?branch=master)](https://travis-ci.org/kevinushey/sourcetools) [![AppVeyor Build Status](https://ci.appveyor.com/api/projects/status/github/kevinushey/sourcetools?branch=master&svg=true)](https://ci.appveyor.com/project/kevinushey/sourcetools)

%package lib
Summary: lib components for the R-sourcetools package.
Group: Libraries

%description lib
lib components for the R-sourcetools package.


%prep
%setup -q -c -n sourcetools

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492800261

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492800261
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library sourcetools
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library sourcetools


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
/usr/lib64/R/library/sourcetools/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/sourcetools/libs/sourcetools.so
