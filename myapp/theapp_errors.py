ERRORS = {

   # I/O level error codes 1-100
    0:      "XIA_SUCCESS",                             # The routine succeeded.
    1:      "XIA_OPEN_FILE",                           # Error opening file.
    2:      "XIA_FILEERR",                             # File related error.
    3:      "XIA_NOSECTION",                           # Unable to find section in ini file.
    4:      "XIA_FORMAT_ERROR",                        # Syntax error in ini file.
    5:      "XIA_ILLEGAL_OPERATION",                   # Attempted to configure options in an illegal order.
    6:      "XIA_FILE_RA",                             # File random access unable to find name-value pair.
    7:      "XIA_SET_POS",                             # Error getting file position.
    8:      "XIA_READ_ONLY",                           # A write operation when read only.
    9:      "XIA_INVALID_VALUE",                       # The value is invalid.
    10:     "XIA_NOT_IDLE",                            # Handel is not idle so could not complete the request.
    11:     "XIA_NOT_ACTIVE",                          # Handel is idle so could not complete the request.
    12:     "XIA_THREAD_ERROR",                        # Thread related error
    13:     "XIA_PROTOCOL_ERROR",                      # Protocol related error.
    14:     "XIA_ALREADY_OPEN",                        # Already open.
   # Primitive level error codes (due to mdio failures) 101-200

   # DSP/FIPPI level error codes 201-300 
    201:    "XIA_UNKNOWN_DECIMATION",                  # The decimation read from the hardware does not match a known value
    202:    "XIA_SLOWLEN_OOR",                         # Calculated SLOWLEN value is out-of-range
    203:    "XIA_SLOWGAP_OOR",                         # Calculated SLOWGAP value is out-of-range
    204:    "XIA_SLOWFILTER_OOR",                      # Attempt to set the Peaking or Gap time s.t. P+G>31
    205:    "XIA_FASTLEN_OOR",                         # Calculated FASTLEN value is out-of-range
    206:    "XIA_FASTGAP_OOR",                         # Calculated FASTGAP value is out-of-range
    207:    "XIA_FASTFILTER_OOR",                      # Attempt to set the Peaking or Gap time s.t. P+G>31
    208:    "XIA_BASELINE_OOR",                        # Baseline filter length is out-of-range

   # Configuration errors 301-400
    301: "XIA_INITIALIZE",                             # Fatal error on initialization
    302: "XIA_NO_ALIAS",                               # A module, detector, or firmware item with the given alias is not defined.
    303: "XIA_ALIAS_EXISTS",                           # Trying to add a configuration item with existing alias
    304: "XIA_BAD_VALUE",                              # Out of range or invalid input value
    305: "XIA_INFINITE_LOOP",                          # Infinite loop detected
    306: "XIA_BAD_NAME",                               # Specified name is not valid
    307: "XIA_BAD_PTRR",                               # Specified PTRR is not valid for this alias
    308: "XIA_ALIAS_SIZE",                             # Alias name length exceeds #MAXALIAS_LEN
    309: "XIA_NO_MODULE",                              # Must define at least one module before
    310: "XIA_BAD_INTERFACE",                          # The specified interface does not exist
    311: "XIA_NO_INTERFACE",                           # An interface must defined before more information is specified
    312: "XIA_WRONG_INTERFACE",                        # Specified information doesn't apply to this interface
    313: "XIA_NO_CHANNELS",                            # Number of channels for this module is set to 0
    314: "XIA_BAD_CHANNEL",                            # Specified channel index is invalid or out-of-range
    315: "XIA_NO_MODIFY",                              # Specified name cannot be modified once set
    316: "XIA_INVALID_DETCHAN",                        # Specified detChan value is invalid
    317: "XIA_BAD_TYPE",                               # The DetChanElement type specified is invalid
    318: "XIA_WRONG_TYPE",                             # This routine only operates on detChans that are sets
    319: "XIA_UNKNOWN_BOARD",                          # Board type is unknown
    320: "XIA_NO_DETCHANS",                            # No detChans are currently defined
    321: "XIA_NOT_FOUND",                              # Unable to locate the Acquisition value requested
    322: "XIA_PTR_CHECK",                              # Pointer is out of synch when it should be valid
    323: "XIA_LOOKING_PTRR",                           # FirmwareSet has a FDD file defined and this only works with PTRRs
    324: "XIA_NO_FILENAME",                            # Requested filename information is set to NULL
    325: "XIA_BAD_INDEX",                              # User specified an alias index that doesn't exist
    326: "XIA_NULL_ALIAS",                             # Null alias passed into function
    327: "XIA_NULL_NAME",                              # Null name passed into function
    328: "XIA_NULL_VALUE",                             # Null value passed into function
    329: "XIA_NEEDS_BOARD_TYPE",                       # Module needs board_type
    330: "XIA_UNKNOWN_ITEM",                           # Unknown item
    331: "XIA_TYPE_REDIRECT",                          # Module type can not be redefined once set
    332: "XIA_NO_TMP_PATH",                            # No FDD temporary path defined for this firmware.
    333: "XIA_NULL_PATH",                              # Specified path was NULL.

   # Config errors found by xiaStartSystem(). 350-400
    350: "XIA_FIRM_BOTH",                           # A FirmwareSet may not contain both an FDD and seperate Firmware definitions
    351: "XIA_PTR_OVERLAP",                         # Peaking time ranges in the Firmware definitions may not overlap
    352: "XIA_MISSING_FIRM",                        # Either the FiPPI or DSP file is missing from a Firmware element
    353: "XIA_MISSING_POL",                         # A polarity value is missing from a Detector element
    354: "XIA_MISSING_GAIN",                        # A gain value is missing from a Detector element
    355: "XIA_MISSING_INTERFACE",                   # The interface this channel requires is missing
    356: "XIA_MISSING_ADDRESS",                     # The epp_address information is missing for this channel
    357: "XIA_INVALID_NUMCHANS",                    # The wrong number of channels are assigned to this module
    358: "XIA_INCOMPLETE_DEFAULTS",                 # Some of the required defaults are missing
    359: "XIA_BINS_OOR",                            # There are too many or too few bins for this module type
    360: "XIA_MISSING_TYPE",                        # The type for the current detector is not specified properly
    361: "XIA_NO_MMU",                              # No MMU defined and/or required for this module
    362: "XIA_NULL_FIRMWARE",                       # No firmware set defined
    363: "XIA_NO_FDD",                              # No FDD defined in the firmware set

   # Host machine error codes 401-500
    401: "XIA_NOMEM",                              # Unable to allocate memory
    402: "XIA_XERXES_DEPRECATED",                  # XerXes returned an error. Check log error output.
    403: "XIA_MD",                                 # MD layer returned an error
    404: "XIA_EOF",                                # EOF encountered
    405: "XIA_BAD_FILE_READ",                      # File read failed
    406: "XIA_BAD_FILE_WRITE",                     # File write failed

   # Miscellaneous errors 501-600
    501: "XIA_UNKNOWN",
    506: "XIA_LOG_LEVEL",                          # Log level invalid
    507: "XIA_FILE_TYPE",                          # Improper file type specified
    508: "XIA_END",                                # There are no more instances of the name specified. Pos set to end
    509: "XIA_INVALID_STR",                        # Invalid string format
    510: "XIA_UNIMPLEMENTED",                      # The routine is unimplemented in this version
    511: "XIA_PARAM_DEBUG_MISMATCH",               # A parameter mismatch was found with XIA_PARAM_DEBUG enabled.

   # PSL errors 601-700
    601: "XIA_NOSUPPORT_FIRM",                     # The specified firmware is not supported by this board type
    602: "XIA_UNKNOWN_FIRM",                       # The specified firmware type is unknown
    603: "XIA_NOSUPPORT_VALUE",                    # The specified acquisition value is not supported
    604: "XIA_UNKNOWN_VALUE",                      # The specified acquisition value is unknown
    605: "XIA_PEAKINGTIME_OOR",                    # The specified peaking time is out-of-range for this product
    606: "XIA_NODEFINE_PTRR",                      # The specified peaking time does not have a PTRR associated with it
    607: "XIA_THRESH_OOR",                         # The specified treshold is out-of-range
    608: "XIA_ERROR_CACHE",                        # The data in the values cache is out-of-sync
    609: "XIA_GAIN_OOR",                           # The specified gain is out-of-range for this produce
    610: "XIA_TIMEOUT",                            # Timeout waiting for BUSY
    611: "XIA_BAD_SPECIAL",                        # The specified special run is not supported for this module
    612: "XIA_TRACE_OOR",                          # The specified value of tracewait (in ns) is out-of-range
    613: "XIA_DEFAULTS",                           # The PSL layer encountered an error creating a Defaults element
    614: "XIA_BAD_FILTER",                         # Error loading filter info from either a FDD file or the Firmware configuration
    615: "XIA_NO_REMOVE",                          # Specified acquisition value is required for this product and can't be removed
    616: "XIA_NO_GAIN_FOUND",                      # Handel was unable to converge on a stable gain value
    617: "XIA_UNDEFINED_RUN_TYPE",                 # Handel does not recognize this run type
    618: "XIA_INTERNAL_BUFFER_OVERRUN",            # Handel attempted to overrun an internal buffer boundry
    619: "XIA_EVENT_BUFFER_OVERRUN",               # Handel attempted to overrun the event buffer boundry
    620: "XIA_BAD_DATA_LENGTH",                    # Handel was asked to set a Data length to zero for readout
    621: "XIA_NO_LINEAR_FIT",                      # Handel was unable to perform a linear fit to some data
    622: "XIA_MISSING_PTRR",                       # Required PTRR is missing
    623: "XIA_PARSE_DSP",                          # Error parsing DSP
    624: "XIA_UDXPS",
    625: "XIA_BIN_WIDTH",                          # Specified bin width is out-of-range
    626: "XIA_NO_VGA",                             # An attempt was made to set the gaindac on a board that doesn't have a VGA
    627: "XIA_TYPEVAL_OOR",                        # Specified detector type value is out-of-range
    628: "XIA_LOW_LIMIT_OOR",                      # Specified low MCA limit is out-of-range
    629: "XIA_BPB_OOR",                            # bytes_per_bin is out-of-range
    630: "XIA_FIP_OOR",                            # Specified FiPPI is out-of-range
    631: "XIA_MISSING_PARAM",                      # Unable to find DSP parameter in list
    632: "XIA_OPEN_XW",                            # Error opening a handle in the XW library
    633: "XIA_ADD_XW",                             # Error adding to a handle in the XW library
    634: "XIA_WRITE_XW",                           # Error writing out a handle in the XW library
    635: "XIA_VALUE_VERIFY",                       # Returned value inconsistent with sent value
    636: "XIA_POL_OOR",                            # Specifed polarity is out-of-range
    637: "XIA_SCA_OOR",                            # Specified SCA number is out-of-range
    638: "XIA_BIN_MISMATCH",                       # Specified SCA bin is either too high or too low
    639: "XIA_WIDTH_OOR",                          # MCA bin width is out-of-range
    640: "XIA_UNKNOWN_PRESET",                     # Unknown PRESET run type specified
    641: "XIA_GAIN_TRIM_OOR",                      # Gain trim out-of-range
    642: "XIA_GENSET_MISMATCH",                    # Returned GENSET doesn't match the set GENSET
    643: "XIA_NUM_MCA_OOR",                        # The specified number of MCA bins is out of range
    644: "XIA_PEAKINT_OOR",                        # The specified value for PEAKINT is out of range.
    645: "XIA_PEAKSAM_OOR",                        # The specified value for PEAKSAM is out of range.
    646: "XIA_MAXWIDTH_OOR",                       # The specified value for MAXWIDTH is out of range.
    647: "XIA_NULL_TYPE",                          # A NULL file type was specified
    648: "XIA_GAIN_SCALE",                         # Gain scale factor is not valid
    649: "XIA_NULL_INFO",                          # The specified info array is NULL
    650: "XIA_UNKNOWN_PARAM_DATA",                 # Unknown parameter data type
    651: "XIA_MAX_SCAS",                           # The specified number of SCAs is more then the maximum allowed
    652: "XIA_UNKNOWN_BUFFER",                     # Requested buffer is unknown
    653: "XIA_NO_MAPPING",                         # Mapping mode is currently not installed/enabled
    654: "XIA_CLRBUFFER_TIMEOUT",                  # Time out waiting for buffer to clear
    655: "XIA_UNKNOWN_PT_CTL",                     # Unknown mapping point control.
    656: "XIA_CLOCK_SPEED",                        # The hardware is reporting an invalid clock speed.
    657: "XIA_BAD_DECIMATION",                     # Passed in decimation is invalid.
    658: "XIA_BAD_SYNCH_RUN",                      # Specified value for synchronous run is bad.
    659: "XIA_PRESET_VALUE_OOR",                   # Requested preset value is out-of-range.
    660: "XIA_MEMORY_LENGTH",                      # Memory length is invalid.
    661: "XIA_UNKNOWN_PREAMP_TYPE",                # Preamp type is unknown.
    662: "XIA_DAC_TARGET_OOR",                     # The specified DAC target is out of range.
    663: "XIA_DAC_TOL_OOR",                        # The specified DAC tolerance is out of range.
    664: "XIA_BAD_TRIGGER",                        # Specified trigger setting is invalid.
    665: "XIA_EVENT_LEN_OOR",                      # The specified event length is out of range.
    666: "XIA_PRE_BUF_LEN_OOR",                    # The specified pre-buffer length is out of range.
    667: "XIA_HV_OOR",                             # The specified high voltage value is out of range.
    668: "XIA_PEAKMODE_OOR",                       # The specified peak mode is out of range.
    669: "XIA_NOSUPPORTED_PREAMP_TYPE",            # The specified preamp type is not supported by current firmware.
    670: "XIA_ENERGYCOEF_OOR",                     # The calculated energy coefficient values are out of range.
    671: "XIA_VETO_PULSE_STEP",                    # The specified step value is too large for the Alpha pulser veto pulse.
    672: "XIA_TRIGOUTPUT_OOR",                     # The specified trigger signal output is out of range.
    673: "XIA_LIVEOUTPUT_OOR",                     # The specified livetime signal output is out of range.
    674: "XIA_UNKNOWN_MAPPING",                    # Unknown mapping mode value specified.
    675: "XIA_UNKNOWN_LIST_MODE_VARIANT",          # Illegal list mode variant.
    676: "XIA_MALFORMED_LENGTH",                   # List mode upper length word is malformed.
    677: "XIA_CLRBUFSIZE_LENGTH",                  # Clear Buffer Size length is too large.
    678: "XIA_BAD_ELECTRODE_SIZE",                 # UltraLo electrode size is invalid.
    679: "XIA_TILT_THRESHOLD_OOR",                 # Specified threshold is out-of-range.
    680: "XIA_USB_BUSY",                           # Direct USB command failed due to busy USB.
    681: "XIA_MALFORMED_MM_RESPONSE",              # UltraLo moisture meter response is malformed.
    682: "XIA_MALFORMED_MM_STATUS",                # UltraLo moisture meter status is invalid.
    683: "XIA_MALFORMED_MM_VALUE",                 # UltraLo moisture meter value is invalid.
    684: "XIA_NO_EVENTS",                          # No events to retrieve from the event buffer.
    685: "XIA_NOSUPPORT_RUNDATA",                  # The specified run data is not supported
    686: "XIA_PARAMETER_OOR",                      # The parameter passed in is out of range.
    687: "XIA_PASSTHROUGH",                        # UART passthrough command error
    688: "XIA_UNSUPPORTED",                        # Feature unsupported by current hardware

   # handel-sitoro errors 690-700
    690: "XIA_DAC_GAIN_OOR",                       # SiToro DAC gain is out of range.
    691: "XIA_NO_SPECTRUM",                        # No spectrum has been received.

   # XUP errors 701-800
    701: "XIA_XUP_VERSION",                        # XUP version is not supported
    702: "XIA_CHKSUM",                             # checksum mismatch in the XUP
    704: "XIA_SIZE_MISMATCH",                      # Size read from file is incorrect
    705: "XIA_NO_ACCESS",                          # Specified access file isn't valid
    706: "XIA_N_FILTER_BAD",                       # The number of filter parameters in the FDD doesn't match the number requires for the hardware

   # Additional PSL errors used in handel-sitoro 802-900
    802: "XIA_ACQ_OOR",                            # Generic acquisition value conversion out of range.
    803: "XIA_ENCODE",                             # Base64 encoding error.
    804: "XIA_DECODE",                             # Base64 decoding error.
    805: "XIA_BAD_PSL_ARGS",                       # Bad call arguments to PSL function.

   # I/O level error codes 4001-4100
    4001: "DXP_MDOPEN"             ,# Error opening port for communication
    4002: "DXP_MDIO"               ,# Device IO error
    4003: "DXP_MDINITIALIZE"       ,# Error configurting port during initialization
    4007: "DXP_MDSIZE"             ,# Incoming data packet length larger than requested
    4009: "DXP_MDUNKNOWN"          ,# Unknown IO function
    4010: "DXP_MDCLOSE"            ,# Error closing connection
    4012: "DXP_MDINVALIDPRIORITY"  ,# Invalid priority type
    4013: "DXP_MDPRIORITY"         ,# Error setting priority
    4014: "DXP_MDINVALIDNAME"      ,# Error parsing IO name
    4018: "DXP_MD_TARGET_ADDR"     ,# Invalid target address
    4019: "DXP_OPEN_EPP"           ,# Unable to open EPP port
    4020: "DXP_BAD_IONAME"         ,# Invalid io name format
    4020: "DXP_UNKONWN_BAUD"       ,# Unknown baud rate

    # Saturn specific error codes
    4101: "DXP_WRITE_TSAR"         ,# Error writing TSAR register
    4102: "DXP_WRITE_CSR"          ,# Error writing CSR register
    4103: "DXP_WRITE_WORD"         ,# Error writing single word
    4104: "DXP_READ_WORD"          ,# Error reading single word
    4105: "DXP_WRITE_BLOCK"        ,# Error writing block data
    4106: "DXP_READ_BLOCK"         ,# Error reading block data
    4110: "DXP_READ_CSR"           ,# Error reading CSR register
    4111: "DXP_WRITE_FIPPI"        ,# Error writing to FIPPI
    4112: "DXP_WRITE_DSP"          ,# Error writing to DSP
    4115: "DXP_DSPSLEEP"           ,# Error with DSP Sleep
    4116: "DXP_NOFIPPI"            ,# No valid FiPPI defined
    4117: "DXP_FPGADOWNLOAD"       ,# Error downloading FPGA
    4118: "DXP_DSPLOAD"            ,# Error downloading DSP
    4119: "DXP_DSPACCESS"          ,# Specified DSP parameter is read-only
    4120: "DXP_DSPPARAMBOUNDS"     ,# DSP parameter value is out of range
    4122: "DXP_NOCONTROLTYPE"      ,# Unknown control task
    4123: "DXP_CONTROL_TASK"       ,# Control task parameter error

    # microDXP errors
    4140: "DXP_STATUS_ERROR"       ,# microDXP device status error
    4141: "DXP_DSP_ERROR"          ,# microDXP DSP status error
    4142: "DXP_PIC_ERROR"          ,# microDXP PIC status error
    4143: "DXP_UDXP_RESPONSE"      ,# microDXP response error
    4144: "DXP_MISSING_ESC"        ,# microDXP response is missing ESCAPE char

    # DSP/FIPPI level error codes 4201-4300
    4201: "DXP_DSPRUNERROR"       ,# Error decoding run error
    4202: "DXP_NOSYMBOL"          ,# Unknown DSP parameter
    4203: "DXP_TIMEOUT"           ,# Time out waiting for DSP to be ready
    4204: "DXP_DSP_RETRY"         ,# DSP failed to download after multiple attempts
    4205: "DXP_CHECKSUM"          ,# Error verifing checksum
    4206: "DXP_BAD_BIT"           ,# Requested bit is out-of-range
    4207: "DXP_RUNACTIVE"         ,# Run already active in module
    4208: "DXP_INVALID_STRING"   ,# Invalid memory string format
    4209: "DXP_UNIMPLEMENTED"    ,# Requested function is unimplemented
    4210: "DXP_MEMORY_LENGTH"    ,# Invalid memory length
    4211: "DXP_MEMORY_BLK_SIZE"  ,# Invalid memory block size
    4212: "DXP_UNKNOWN_MEM"      ,# Unknown memory type
    4213: "DXP_UNKNOWN_FPGA"     ,# Unknown FPGA type
    4214: "DXP_FPGA_TIMEOUT"     ,# Time out downloading FPGA
    4215: "DXP_APPLY_STATUS"     ,# Error applying change
    4216: "DXP_INVALID_LENGTH"   ,# Specified length is invalid
    4217: "DXP_NO_SCA"           ,# No SCAs defined for the specified channel
    4218: "DXP_FPGA_CRC"         ,# CRC error after FPGA downloaded
    4219: "DXP_UNKNOWN_REG"      ,# Unknown register
    4220: "DXP_OPEN_FILE"        ,# UNable to open firmware file
    4221: "DXP_REWRITE_FAILURE"  ,# Couldn't set parameter even after n iterations.

    # Xerxes onfiguration errors 4301-4400
    4301: "DXP_BAD_SYSTEMITEM"   ,# Invalid system item format
    4302: "DXP_MAX_MODULES"      ,# Too many modules specified
    4303: "DXP_NODETCHAN"        ,# Detector channel is unknown
    4304: "DXP_NOIOCHAN"         ,# IO Channel is unknown
    4305: "DXP_NOMODCHAN"        ,# Modchan is unknown
    4306: "DXP_NEGBLOCKSIZE"     ,# Negative block size unsupported
    4307: "DXP_INITIALIZE"    ,# Initialization error
    4308: "DXP_UNKNOWN_BTYPE"    ,# Unknown board type
    4309: "DXP_BADCHANNEL"       ,# Invalid channel number
    4310: "DXP_NULL"             ,# Parameter cannot be NULL
    4311: "DXP_MALFORMED_FILE"   ,# Malformed firmware file
    4312: "DXP_UNKNOWN_CT"       ,# Unknown control task

    # Host machine error codes 4401-4500
    4401: "DXP_NOMEM"            ,# Error allocating memory
    4402: "DXP_WIN32_API"        ,# Windows API error

    # Misc error codes 501-600
    4501: "DXP_LOG_LEVEL"        # Log level invalid
}