Summary:	bash-completion for PEAR
Summary(pl.UTF-8):	bashowe uzupełnianie nazw dla PEAR
Name:		bash-completion-pear
Version:	0.20080727
Release:	1
License:	GPL
Group:		Applications/Shells
Source0:	http://gluegadget.com/misc/pear
# NoSource0-md5:
URL:		http://gluegadget.com/blog/index.php?/archives/27-PEAR-bash-completion.html
Requires:	bash-completion
Requires:	php-pear-PEAR
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir /etc/bash_completion.d

%description
bash-completion for PEAR.

%description -l pl.UTF-8
bashowe uzupełnianie nazw dla PEAR.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -D %{SOURCE0} $RPM_BUILD_ROOT%{_sysconfdir}/pear-completion

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_sysconfdir}/*
