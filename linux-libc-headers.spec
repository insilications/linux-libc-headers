#
# This package has the headers for glibc.
# Although these come from the kernel, they are not kernel headers.
# These headers describe the kernel <-> userspace API/ABI for glibc use (only).
# As such, this package does not track the upstream kernel-of-the-day,
# and sticks to stable points of Linus releases.
#
# Usually we like to stick to LTS releases for these headers
#
# If you want to update this package, it needs a valid reason (like a new kernel
# API/ABI you want to use) and likely a glibc rebuild following updating this package
#

#
# If you have an out of tree driver that adds a userspace interface, we feel sorry
# for your pain, but this is not the place to add your unofficial permanent ABI.
# You will need to add a copy of your unofficial ABI to the package(s) that need
# to use this unofficial ABI, and those packages will need to be recompiled
# if the ABI changes as part of your upstreaming process.
#



Name:           linux-libc-headers
Version:        5.13
Release:        20
License:        GPL-2.0
Summary:        Headers for the C library that describe the kernel/userspace ABI
Url:            https://www.kernel.org/
Group:          devel
Source0:        https://www.kernel.org/pub/linux/kernel/v5.x/linux-5.13.1.tar.xz

BuildRequires: bison
BuildRequires: flex
BuildRequires: rsync

%description
Headers for the C library that describe the kernel/userspace ABI.


%prep
%setup -q -n linux-%{version}.1

%build
make allnoconfig %{?_smp_mflags}

%install
make headers_install INSTALL_HDR_PATH=%{buildroot}/usr
# Kernel should not be exporting this header
rm -f %{buildroot}//usr/include/scsi/scsi.h
# The ..install.cmd conflicts between various configure runs
find %{buildroot}/usr/include -name ..install.cmd | xargs rm -f || :

%files 
/usr/include/asm-generic/*
/usr/include/asm/*
/usr/include/drm/*
/usr/include/linux/*
/usr/include/mtd/*
/usr/include/rdma/*
/usr/include/scsi/*
/usr/include/sound/*
/usr/include/video/*
/usr/include/xen/*
/usr/include/misc/cxl.h
/usr/include/misc/ocxl.h
/usr/include/misc/fastrpc.h
/usr/include/misc/habanalabs.h
/usr/include/misc/xilinx_sdfec.h
/usr/include/misc/pvpanic.h
/usr/include/misc/uacce/hisi_qm.h
/usr/include/misc/uacce/uacce.h
