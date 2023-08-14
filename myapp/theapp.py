from ctypes import *

libhandel = cdll.LoadLibrary("./myapp/lib/libhandel.so")

ERRORS = {
    0:      "XIA_SUCCESS",
    1:      "XIA_OPEN_FILE",
    2:      "XIA_FILEERR",
    3:      "XIA_NOSECTION",
    4:      "XIA_FORMAT_ERROR",
    5:      "XIA_ILLEGAL_OPERATION",
    6:      "XIA_FILE_RA",
    7:      "XIA_SET_POS",
    8:      "XIA_READ_ONLY",
    9:      "XIA_INVALID_VALUE",
    10:     "XIA_NOT_IDLE",
    11:     "XIA_NOT_ACTIVE",
    12:     "XIA_THREAD_ERROR",
    13:     "XIA_PROTOCOL_ERROR",
    14:     "XIA_ALREADY_OPEN"
}

# DEBUGLEVELS = {
#     1:  "MD_ERROR",
#     2:  "MD_WARNING",
#     3:  "MD_INFO",
#     4:  "MD_DEBUG"
# }

# The C printf function is expecting byte strings. In Python 3 all strings are unicode so you'll have to encode to bytes (https://stackoverflow.com/a/8544421/16173155)
def stringToBytes(mystring):
    return mystring.encode('ascii')

libhandel.xiaSetLogLevel(4)
libhandel.xiaSetLogOutput(stringToBytes("myapp/handel.log"))

print("Loading system... \t", end='')
status = libhandel.xiaInit(stringToBytes("myapp/microdxp_usb2.ini"))
print("Status: " + str(status) + ", " + str(ERRORS.get(status)))

print("Starting system... \t", end='')
status = libhandel.xiaStartSystem()
print("Status: " + str(status) + ", " + str(ERRORS.get(status)))
