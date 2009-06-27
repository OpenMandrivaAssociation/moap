Name:		moap
Version:	0.2.7
Release:	%mkrel 1
Summary:	A tool to help project mainteners to manage releases
License:	GPL
Group:      Development/Python		
URL:		https://thomas.apestaart.org/moap/trac/
Source:		http://thomas.apestaart.org/download/moap/%{name}-%{version}.tar.bz2
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Buildrequires:	python-devel
BuildArch:      noarch
%description
Moap is a swiss army knife for project maintainers and developers. It aims to 
help in keeping you in the flow of maintaining, developing and releasing, 
automating whatever tasks can be automated. This includes updating and 
committing from ChangeLog files (much like prepare-ChangeLog.pl), maintaining 
your checkout's ignore list, submitting releases to Freshmeat, sending out 
release mails (with support for templating), creating iCal/RSS feeds for your 
releases (based on a doap file, and with support for templating), and more.

Supported version control systems currently are Bazaar, CVS, darcs, git and 
Subversion. Supported templating languages are Cheetah and Genshi. Supported 
bug tracker backends are Bugzilla and Trac.

%prep
%setup -q

%build
# force the libdir value, or package is no longer a proper noarch
%configure 
%make

%install
rm -rf %{buildroot}
%makeinstall libdir=%{buildroot}/%{_prefix}/lib/ 

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog AUTHORS README COPYING HACKING 
%doc INSTALL NEWS RELEASE TODO     
%{_bindir}/*
%{py_puresitedir}/%{name}
%{_sysconfdir}/bash_completion.d/*
%{_mandir}/man1/*
