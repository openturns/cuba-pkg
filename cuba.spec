Name:           cuba
Version:        4.2.2
Release:        1%{?dist}
Summary:        A library for multidimensional numerical integration
Group:          System Environment/Libraries
License:        LGPL3
URL:            https://feynarts.de/cuba/
Source0:        https://feynarts.de/cuba/Cuba-%{version}.tar.gz
Patch0:         0001-Add-CMake-script.patch
BuildRequires:  gcc-c++, cmake

%description
A library for multidimensional numerical integration.

%package devel
Summary:        A library for multidimensional numerical integration
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

%description devel
A library for multidimensional numerical integration (development files)

%prep
%setup -q -n Cuba-%{version}
%patch0 -p1

%build
%cmake .
%cmake_build

%install
%cmake_install

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/cuba.h
%{_libdir}/*.so

%changelog
* Thu May 02 2024 Julien Schueller <schueller at phimeca dot com> 4.2.2-1
- Initial package creation
