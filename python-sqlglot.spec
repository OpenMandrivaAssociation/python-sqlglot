Name:		python-sqlglot
Version:	30.20.0
Release:	1
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

%files
%{py_sitedir}/*
