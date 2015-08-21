%define		snap	20150817
%define		plugin	python-pep8-indent
Summary:	Vim plugin: Python pep8 indent
Name:		vim-plugin-%{plugin}
Version:	0.1
Release:	0.%{snap}.1
License:	CC0 1.0 Universal
Group:		Applications/Editors/Vim
Source0:	https://github.com/hynek/vim-python-pep8-indent/archive/master.tar.gz
# Source0-md5:	8b1174311aedccb17807c9cac7c5baee
URL:		https://github.com/hynek/vim-python-pep8-indent
Requires:	vim-rt >= 4:6.3.058-3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim/vimfiles

%description
A nicer Python indentation style for Vim.

%prep
%setup -q -n vim-%{plugin}-master

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/indent
cp -p indent/python.vim $RPM_BUILD_ROOT%{_vimdatadir}/indent

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.rst CONTRIBUTING.rst README.rst 
%{_vimdatadir}/indent/python.vim
