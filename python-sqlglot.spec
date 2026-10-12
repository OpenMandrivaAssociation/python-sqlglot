Name:		python-sqlglot
Version:	30.20.0
Release:	2
Summary:	An easily customizable SQL parser and transpiler
License:	MIT
Group:		Development/Python
URL:		https://pypi.org/project/sqlglot/
Source0:	sqlglot-30.20.0.tar.gz
BuildSystem:	python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildArch:	noarch
%description
An easily customizable SQL parser and transpiler.

%build -p
# The sdist is not a git checkout, so the versioning backend needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%{py_sitedir}/*
