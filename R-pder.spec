#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pder
Version  : 1.0.1
Release  : 2
URL      : https://cran.r-project.org/src/contrib/pder_1.0-1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pder_1.0-1.tar.gz
Summary  : Panel Data Econometrics with R
Group    : Development/Tools
License  : GPL-2.0+
BuildRequires : buildreq-R
BuildRequires : util-linux

%description
No detailed description available

%prep
%setup -q -c -n pder

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571874663

%install
export SOURCE_DATE_EPOCH=1571874663
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
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
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pder
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pder
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pder
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc pder || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pder/DESCRIPTION
/usr/lib64/R/library/pder/INDEX
/usr/lib64/R/library/pder/Meta/Rd.rds
/usr/lib64/R/library/pder/Meta/data.rds
/usr/lib64/R/library/pder/Meta/features.rds
/usr/lib64/R/library/pder/Meta/hsearch.rds
/usr/lib64/R/library/pder/Meta/links.rds
/usr/lib64/R/library/pder/Meta/nsInfo.rds
/usr/lib64/R/library/pder/Meta/package.rds
/usr/lib64/R/library/pder/NAMESPACE
/usr/lib64/R/library/pder/data/CallBacks.rda
/usr/lib64/R/library/pder/data/CoordFailure.rda
/usr/lib64/R/library/pder/data/DemocracyIncome.rda
/usr/lib64/R/library/pder/data/DemocracyIncome25.rda
/usr/lib64/R/library/pder/data/Dialysis.rda
/usr/lib64/R/library/pder/data/Donors.rda
/usr/lib64/R/library/pder/data/EvapoTransp.rda
/usr/lib64/R/library/pder/data/FinanceGrowth.rda
/usr/lib64/R/library/pder/data/ForeignTrade.rda
/usr/lib64/R/library/pder/data/GiantsShoulders.rda
/usr/lib64/R/library/pder/data/HousePricesUS.rda
/usr/lib64/R/library/pder/data/IncomeMigrationH.rda
/usr/lib64/R/library/pder/data/IncomeMigrationV.rda
/usr/lib64/R/library/pder/data/IneqGrowth.rda
/usr/lib64/R/library/pder/data/LandReform.rda
/usr/lib64/R/library/pder/data/LateBudgets.rda
/usr/lib64/R/library/pder/data/Mafia.rda
/usr/lib64/R/library/pder/data/MagazinePrices.rda
/usr/lib64/R/library/pder/data/RDPerfComp.rda
/usr/lib64/R/library/pder/data/RDSpillovers.rda
/usr/lib64/R/library/pder/data/Reelection.rda
/usr/lib64/R/library/pder/data/RegIneq.rda
/usr/lib64/R/library/pder/data/ScrambleAfrica.rda
/usr/lib64/R/library/pder/data/SeatBelt.rda
/usr/lib64/R/library/pder/data/Seniors.rda
/usr/lib64/R/library/pder/data/Solow.rda
/usr/lib64/R/library/pder/data/TexasElectr.rda
/usr/lib64/R/library/pder/data/Tileries.rda
/usr/lib64/R/library/pder/data/TobinQ.rda
/usr/lib64/R/library/pder/data/TradeEU.rda
/usr/lib64/R/library/pder/data/TradeFDI.rda
/usr/lib64/R/library/pder/data/TurkishBanks.rda
/usr/lib64/R/library/pder/data/TwinCrises.rda
/usr/lib64/R/library/pder/data/datalist
/usr/lib64/R/library/pder/data/etw.rda
/usr/lib64/R/library/pder/data/usaw46.rda
/usr/lib64/R/library/pder/data/usaw49.rda
/usr/lib64/R/library/pder/help/AnIndex
/usr/lib64/R/library/pder/help/aliases.rds
/usr/lib64/R/library/pder/help/paths.rds
/usr/lib64/R/library/pder/help/pder.rdb
/usr/lib64/R/library/pder/help/pder.rdx
/usr/lib64/R/library/pder/html/00Index.html
/usr/lib64/R/library/pder/html/R.css
