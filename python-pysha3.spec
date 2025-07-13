#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (incompatible with 3.9+, see python3-safe-pysha3.spec instead)

Summary:	SHA-3 (Keccak) for Python 2
Summary(pl.UTF-8):	SHA-3 (Keccak) dla Pythona 2
Name:		python-pysha3
Version:	1.0.2
Release:	1
License:	PSF v2, CC0 v1.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pysha3/
Source0:	https://files.pythonhosted.org/packages/source/p/pysha3/pysha3-%{version}.tar.gz
# Source0-md5:	59cd2db7a9988c1f3f6aee40145e0c96
URL:		https://pypi.org/project/pysha3/
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-devel < 1:3.9
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
SHA-3 wrapper (keccak) for Python. The package is a wrapper around the
optimized Keccak Code Package,
<https://github.com/gvanas/KeccakCodePackage>.

%description -l pl.UTF-8
Obudowanie SHA-3 (keccak) dla Pythona. Pakiet obudowuje
zoptymalizowany kod Keccak Code Package
<https://github.com/gvanas/KeccakCodePackage>.

%package -n python3-pysha3
Summary:	SHA-3 (Keccak) for Python 3
Summary(pl.UTF-8):	SHA-3 (Keccak) dla Pythona 3
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pysha3
SHA-3 wrapper (keccak) for Python. The package is a wrapper around the
optimized Keccak Code Package,
<https://github.com/gvanas/KeccakCodePackage>.

%description -n python3-pysha3 -l pl.UTF-8
Obudowanie SHA-3 (keccak) dla Pythona. Pakiet obudowuje
zoptymalizowany kod Keccak Code Package
<https://github.com/gvanas/KeccakCodePackage>.

%prep
%setup -q -n pysha3-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-2/lib.*) \
%{__python} tests.py
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
%{__python3} tests.py
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%attr(755,root,root) %{py_sitedir}/_pysha3.so
%{py_sitedir}/sha3.py[co]
%{py_sitedir}/pysha3-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pysha3
%defattr(644,root,root,755)
%doc CHANGES.txt README.txt
%attr(755,root,root) %{py3_sitedir}/_pysha3.cpython-*.so
%{py3_sitedir}/sha3.py
%{py3_sitedir}/__pycache__/sha3.cpython-*.py[co]
%{py3_sitedir}/pysha3-%{version}-py*.egg-info
%endif
