Summary:	HPI GUI application based on Qt4
Summary(pl.UTF-8):	Oparta na Qt4 aplikacja GUI do HPI
Name:		hpibrowser
Version:	2.15.0
Release:	0.1
License:	BSD
Group:		Applications/System
Source0:	http://downloads.sourceforge.net/openhpi/%{name}-%{version}.tar.gz
# Source0-md5:	5e4646a60e0c88a563699c424cc0ddc5
URL:		http://www.openhpi.org/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	QtGui-devel >= 4
BuildRequires:	openhpi-devel >= 2.15.0
BuildRequires:	libstdc++-devel >= 5:4.0
BuildRequires:	qt4-qmake >= 4
BuildRequires:	sed >= 4.0
Requires:	openhpi-libs >= 2.15.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
hpibrowser is a simple Qt4-based GUI application for browsing a HPI
system. It uses OpenHPI client library for Service Availability
Forum's Hardware Platform Interface B.03.02 service.

%description -l pl.UTF-8
hpibrowser to prosta aplikacja z opartym na Qt4 graficznym interfejsem
użytkownika, służąca do przeglądania systemu HPI. Wykorzystuje
bibliotekę kliencką OpenHPI do dostępu do usługi Hardware Platform
Interface B.03.02 zdefiniowanej przez Service Availability Forum.

%prep
%setup -q

sed -i  -e 's,^\(OPENHPI_PREFIX =\).*,\1 /usr,' \
	-e  's,^\(PREFIX = \).*,\1 %{_prefix},' application.pro

%build
qmake-qt4 \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"
	
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING README
%attr(755,root,root) %{_bindir}/hpibrowser
