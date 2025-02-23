- [1. Linux](#1-linux)
  - [1.1. Makefile reference](#11-makefile-reference)
  - [1.2. SCons dev setup](#12-scons-dev-setup)
  - [1.3. Requirements](#13-requirements)
    - [1.3.1. Optional: Handel's test suite requires Ruby](#131-optional-handels-test-suite-requires-ruby)
    - [1.3.2. Building with SCons](#132-building-with-scons)
    - [1.3.3. Notes](#133-notes)
  - [1.4. Defines](#14-defines)
  - [1.5. USB Setup](#15-usb-setup)
    - [1.5.1. Troubleshooting](#151-troubleshooting)
  - [1.6. Serial Port Setup](#16-serial-port-setup)
- [2. Windows](#2-windows)
  - [2.1. Building with SCons](#21-building-with-scons)

# 1. Linux

XIA builds Handel with SCons (stock) + swtoolkit (slightly modified).

The SCons build makes heavy use of static libraries and produces one shared
library for the Handel API and a shared library for each driver protocol (e.g.
xia_usb2 and xia_plx).

This document lists the steps to get Handel building on Linux with those tools
and the default structure. However, you can also skip SCons and integrate with
your own build system with any library structure you like.

## 1.1. Makefile reference

For a non-SCons reference, here is a sample Makefile from a Handel user that
sets flags and source lists for a previous version of Handel:
https://subversion.xray.aps.anl.gov/synApps/dxp/trunk/dxpApp/handelSrc/Makefile

## 1.2. SCons dev setup

The latest version of SCons and swtoolkit are only compatible with python3

## 1.3. Requirements

A working 64bit conda install. Running on the Raspberry Pi 4 using an e.g. [https://github.com/conda-forge/miniforge](https://github.com/conda-forge/miniforge). Then:

```shell
# Create conda environment
conda create -n xmagix python=3.9 pip ipykernel

# Install required python packages
pip install -r requirements.txt

# Install fast GPIO library and activate service
sudo apt-get install pigpio python-pigpio python3-pigpio
sudo pigpiod

# Install other dependencies
sudo apt install libusb-dev
```

### 1.3.1. Optional: Handel's test suite requires Ruby

Apparently, the *test suit* is not part of this repository making this step extra optional.

```shell
sudo apt-get install ruby ruby-dev
```
then
```shell
sudo gem install ffi
```

### 1.3.2. Building with SCons

A build log is output into ``./build.log``

Handel has many flags that map to defines in the compilation environment. A
little experimentation may be needed to get the set that supports only the
products you need.

Here's an example for microDXP USB2:
```shell
TMP=/tmp sh swtoolkit/hammer.sh --udxp --no-udxps --no-xw --no-serial --no-xmap --no-stj --no-mercury --no-saturn --verbose
```

All flags. Taken from ``SetBitFromOption`` in ``./main.scons``.

| Flag       | Description                                  | Default |
| ---------- | -------------------------------------------- | ------- |
| Protocols  |                                              |         |
| `epp`      | Include EPP driver                           | `False` |
| `serial`   | Include RS-232 driver                        | `True`  |
| `usb`      | Include USB driver                           | `False` |
| `usb2`     | Include USB2 driver                          | `True`  |
| `plx`      | Include PLX driver                           | `True`  |
| Devices    |                                              |         |
| `saturn`   | Include Saturn support                       | `True`  |
| `udxp`     | Include microDXP support                     | `True`  |
| `udxps`    | Include microDXP setup support               | `False` |
| `xmap`     | Include xMAP support                         | `True`  |
| `stj`      | Include Stj support                          | `True`  |
| `mercury`  | Include Mercury/Mercury-4 support            | `True`  |
| General    |                                              |         |
| `release`  | Release build                                | `False` |
| `analysis` | Build with code analysis                     | `False` |
| `alpha`    | Build Handel with support for the alpha udxp | `False` |
| `vba`      | Build stdcall dlls for VB applications       | `False` |
| `xw`       | Build xw library                             | `True`  |
| `x64`      | Build Handel for x64 platform                | `False` |
| `tests`    | Build and run tests                          | `False` |
| `samples`  | Build samples                                | `False` |
| `vld`      | Build with Visual Leak Detector              | `False` |

Change options in ``build.sh`` and execute:

```shell
# Make script executable
chmod +x ./build.sh

# Build
./build.sh
```

### 1.3.3. Notes

Chain of script calls:
``build.sh`` → ``./swtoolkit/hammer.sh`` → ``./swtoolkit/wrapper.py`` → ?? → output to ``./scons-out``

Handel dev dependencies:
``export TMP=/tmp # Handel's scons script reads this var?``

## 1.4. Defines

This section lists defines you can use in your build system to control
the features compiled in Handel. Note that not every define is needed
for every file in the source distribution.

Disable products and protocols not currently supported on Linux:
```
EXCLUDE_XMAP EXCLUDE_STJ EXCLUDE_PLX
```

Selectively disable products you do not use:
```
EXCLUDE_MERCURY EXCLUDE_SATURN EXCLUDE_UDXP
```

When building for microDXP, always define these internal feature
exclusions, which are not available in the customer release:
```
EXCLUDE_UDXPS EXCLUDE_XUP
```

Selectively disable interface protocols you do not use:
```
EXCLUDE_SERIAL EXCLUDE_EPP EXCLUDE_USB EXCLUDE_USB2
```


## 1.5. USB Setup

Handel USB and USB2 support on Linux are built on libusb-0.1. If not already done install it using
```shell
sudo apt-get install libusb-dev
```

Check that libusb sees the XIA device:
```shell
lsusb | grep "ID 10e9"
```

The output should be looking something like
```shell
Bus 001 Device 003: ID 10e9:0b01 Cypress EZ-USB
```

By default, root is required to open the device. This snippet shows
how to set up Ubuntu udev rules to enable user access:

```shell
# Confirm your user is in the plugdev group
groups

# Set up udev rules. Customize idProduct for your device as given in second hex pair after 10e9.
sudo echo 'ACTION=="add", SUBSYSTEM=="usb", ATTR{idVendor}=="10e9", ATTRS{idProduct}=="0b01", MODE="0660", GROUP="plugdev"' | sudo tee /etc/udev/rules.d/99-xia.rules

# Reload udev-rules
sudo /etc/init.d/udev restart
```


### 1.5.1. Troubleshooting

If setting udev-rules does not work as expected, one can try debugging using following procedure:

1. Get `<bus_num>`, `<device_num>` and `<device_id>` from `lsusb | grep "ID 10e9"`.
2. Execute `udevadm info -a -n /dev/bus/usb/<bus_num>/<device_num>` where `<bus_num>` and `<device_num>` are obtained from the previous step.
3. Look at the device with `ATTR{idVendor}=="10e9"` and `ATTR{idProduct}=="<device_id>"` (should be the first device). The string after *looking at device* is the `<device_path>`
4. Check `sudo udevadm test <device_path>` for any errors.

It may be helpful in debugging to monitor USB transfers. This is easy
if your system includes usbmon:

```shell
sudo mount -t debugfs none_debugs /sys/kernel/debug
sudo modprobe usbmon
sudo cat /sys/kernel/debug/usb/usbmon/1u | sed -n -e "s/^[a-f0-9]\+ [0-9]\+//p" 2>&1 | tee /tmp/xmagix_usbmon.log
```

## 1.6. Serial Port Setup

Handel v1.2.19 and later includes a serial port implementation built
on termios. This interface is experimental but does pass all microDXP
tests in XIA's testing. To use it, edit the module definition in your
.ini file to set the interface to "serial". Instead of defining
com_port as you would for the Windows serial interface, locate the
device in /dev and put this file in the device\_file setting. Here is
a full sample module definition:

```ini
[module definitions]
START #0
alias = module1
module_type = udxp
interface = serial
device_file = /dev/ttyS1
baud_rate = 230400
number_of_channels = 1
channel0_alias = 0
channel0_detector = detector1:0
firmware_set_chan0 = firmware1
default_chan0 = defaults_module1_0
END #0
```


# 2. Windows

Handel is built with SCons+swtoolkit. The latest version of SCons
and swtoolkit are updated to be compatible with python3

1. Install the latest Python3 Windows installer from [python.org] or
   using Chocolately. The x86-64 version is fine on a 64-bit system.
2. Install required libraries
	pip install -r requirements.txt

Tests in t_api run with Ruby 2.3+. You will need both x86 and x64
versions of Ruby in order to test both builds of Handel. For each
version, `gem install ffi`.


## 2.1. Building with SCons

Handel has many flags that map to defines in the compilation environment. A
little experimentation may be needed to get the set that supports only the
products you need.

The included build script can be used to invoke SCons build environment.

Here's an example for microDXP USB2:
```bash
build --udxp --no-udxps --no-xw --no-serial --no-xmap --no-stj --no-mercury --no-saturn --verbose
```

Another example to build the examples with default option:
```bash
build --samples
```

To search for other flags, search ``SetBitFromOption`` in ``main.scons``.

Resources:

* [python.org](https://www.python.org/downloads/)
* [swtoolkit examples](https://code.google.com/p/swtoolkit/wiki/Examples)
* [swtoolkit glossary](https://code.google.com/p/swtoolkit/wiki/Glossary#COMPONENT_LIBRARY_PUBLISH)
* [SCons manual](http://www.scons.org/doc/production/HTML/scons-man.html)
