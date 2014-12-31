#
# This package has the headers for glibc.
# Although these come from the kernel, they are not kernel headers.
# These headers describe the kernel <-> userspace API/ABI for glibc use (only).
# As such, this package does not track the upstream kernel-of-the-day,
# and sticks to stable points of Linus releases.
#
# If you want to update this package, it needs a valid reason (like a new kernel
# API/ABI you want to use) and likely a glibc rebuild following updating this package
#


Name:           linux-libc-headers
Version:        3.19
Release:        7
License:        GPL-2.0
Summary:        Headers for the C library that describe the kernel/userspace ABI
Url:            https://www.kernel.org/
Group:          devel
Source0:        https://www.kernel.org/pub/linux/kernel/v3.x/linux-3.19.tar.xz

%description
Headers for the C library that describe the kernel/userspace ABI.


%prep
%setup -q -n linux-%{version}

%build
make allnoconfig %{?_smp_mflags}

%install
make headers_install INSTALL_HDR_PATH=%{buildroot}/usr
# Kernel should not be exporting this header
rm -f %{buildroot}/%{_includedir}/scsi/scsi.h
# The ..install.cmd conflicts between various configure runs
find %{buildroot}/%{_includedir} -name ..install.cmd | xargs rm -f

%files 
%{_includedir}/asm-generic/*
%{_includedir}/asm/*
%{_includedir}/drm/*
%{_includedir}/linux/*
%{_includedir}/mtd/*
%{_includedir}/rdma/*
%{_includedir}/scsi/*
%{_includedir}/sound/*
%{_includedir}/video/*
%{_includedir}/xen/*
%{_includedir}/*/.install
/usr/include/misc/cxl.h
