Summary:	owncloud desktop client
Name:		mirall
Version:	1.7.0
Release:	1
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://owncloud.org
Source0:	https://download.owncloud.com/desktop/stable/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(QtWebKit)
BuildRequires:	pkgconfig(neon)
BuildRequires:	qtkeychain-devel
BuildRequires:	pkgconfig(sqlite3)

%description
With ownCloud you can sync & share your files,
calendar, contacts and more.Access your data from
all your devices, on an open platform you can
extend and modify.

%prep
%setup -q

%build
%cmake_qt4
%make

%install
%makeinstall_std -C build

%files
