board_operations_all = [
    "get_serial_number",
        # (char[16]) Get the microDXP board's serial number.
    "get_peaking_time_ranges",
        # (double *) Returns an array of doubles with size (# of FiPPIs * 2). For each FiPPI the shortest peaking time and longest peaking time are returned, in that order.
    "get_number_of_fippis",
        # (unsigned short) Gets the number of FiPPIs that are on the board.
    "get_number_pt_per_fippi",
        # (unsigned short) Gets the number of peaking times in each FiPPI. 5 or 24, depending on the variant.
    "get_current_peaking_times",
        # (double[N]) Get the current peaking times for the selected FiPPI, where the peaking time at index i in the returned list corresponds to PARSET i for the selected FiPPI. N is the number of peaking times per FiPPI, retrieved via board operation get_number_pt_per_fippi.
    "get_peaking_times",
        # (double[N]) Get array of all peaking times supported by the board, in the order of peaking times for each PARSET, often used when the peaking times need to be cached by the application. N can be derived from get_number_of_fippis multiplied by get_number_pt_per_fippi.
    "get_temperature",
        # (double) Returns the current temperature of the board, accurate to 1/16th of a degree of Celsius.
    "apply",
        # (none) Applies the current DSP parameter settings to the hardware. This should be done after modifying any acquisition values.
    "save_parset",
        # (unsigned short) Saves the current DSP parameter settings to the specified PARSET.
    "save_genset",
        # (unsigned short) Saves the current DSP parameter settings to the specified GENSET.
    "set_preset",
        # [Deprecated] (double[2]) Configure a preset run by passing in the preset type and value. The allowed types, defined in handel_constants.h are:
        # • XIA_PRESET_FIXED_REALTIME
        # • XIA_PRESET_FIXED_LIVETIME
        # • XIA_PRESET_FIXED_TRIGGERS
        # • XIA_PRESET_FIXED_EVENTS
        # The values are defined as time in seconds, for the time based runs and counts for the other types.
        # The acquisition values preset_type and preset_value have been implemented to provide r/w access to preset run properties, and should be usedinstead.
    "get_board_info",
        # (unsigned char[26]) Returns the array of board information listed in command 0x49 of the RS-232 Command Reference. The returned data is stored in the array as follows, each line representing a byte. Although the pre-allocated size is fixed, the returned content is dependent on the number of FiPPIs. For products with a single FiPPI,unused bytes can be ignored.
        # -----------------------------
        # 0. PIC Code Variant
        # 1. PIC Code Major Version
        # 2. PIC Code Minor Version
        # 3. DSP Code Variant
        # 4. DSP Code Major Version
        # 5. DSP Code Minor Version
        # 6. DSP Clock Speed
        # 7. Clock Enable Register
        # 8. Number of FiPPIs
        # 9. Gain Mode
        # 10. Gain (mantissa low byte)
        # 11. Gain (mantissa high byte)
        # 12. Gain (exponent)
        # 13. Nyquist Filter
        # 14. ADC Speed Grade
        # 15. FPGA Speed
        # 16. Analog Power Supply
        # 17. FiPPI 0 Decimation
        # 18. FiPPI 0 Version
        # 19. FiPPI 0 Variant
        # -----------------------------
        # Bytes 20-25 repeat the FiPPI pattern for 1 and 2, if available.
    "get_usb_version",
        # (unsigned long) Returns the USB firmware version number packed into an unsigned long as follows: [3]Major [2]Minor [1]Reserved [0]Build. Offsets refer to byte indexes in the unsigned long. For example, the following expression may be used to get the major version: (value >> 24) & 0xFF. This operation is only supported for microDXP firmware Rev H or later and the UltraLo.
    "get_preamp_type",
        # (unsigned short) Returns the current preamplifier type, where 0 = reset and 1 = RC feedback.
    "set_xup_backup_path",
        # (char *) Sets the path where XUP backups are written.
    "get_hardware_status",
        # (unsigned char[5]) Returns the array of status information listed in command 0x4B of the RS-232 Command Reference.
    "passthrough",
        # ({byte*, int*, byte*, int*}) Pass a command through to a UART attached to the processor. This command requires custom hardware and firmware and is not supported on all variants. If the variant does not implement the custom command, xiaBoardOperation will return a Handel error code.
        # The value type is void**, an array pointing to the following elements:
        # • byte* send: an array of bytes to send with the command.
        # • int* send length: number of bytes in the send array.
        # • byte* receive: an array of bytes to return the command response.
        # • int* receive length: number of bytes to read in the command response.
        # Sample usage:
        # byte send[32] = {1, 2, 3};
        # int send_len = sizeof(send) / sizeof(send[0]);
        # byte receive[32] = {0};
        # int receive_len = sizeof(receive) / sizeof(receive[0]);
        # void* value[4] = {send, &send_len, receive, &receive_len};
        # int status = xiaBoardOperation(0, "passthrough", value);
        # CHECK_ERROR(status);
        # /* Process receive... */"
]

board_operations = [
    "get_peaking_time_ranges",
        # (double *) Returns an array of doubles with size (# of FiPPIs * 2). For each FiPPI the shortest peaking time and longest peaking time are returned, in that order.
    "get_number_of_fippis",
        # (unsigned short) Gets the number of FiPPIs that are on the board.
    "get_number_pt_per_fippi",
        # (unsigned short) Gets the number of peaking times in each FiPPI. 5 or 24, depending on the variant.
    "get_current_peaking_times",
        # (double[N]) Get the current peaking times for the selected FiPPI, where the peaking time at index i in the returned list corresponds to PARSET i for the selected FiPPI. N is the number of peaking times per FiPPI, retrieved via board operation get_number_pt_per_fippi.
    "get_peaking_times",
        # (double[N]) Get array of all peaking times supported by the board, in the order of peaking times for each PARSET, often used when the peaking times need to be cached by the application. N can be derived from get_number_of_fippis multiplied by get_number_pt_per_fippi.
    "get_temperature",
        # (double) Returns the current temperature of the board, accurate to 1/16th of a degree of Celsius.
    "save_parset",
        # (unsigned short) Saves the current DSP parameter settings to the specified PARSET.
    "save_genset",
        # (unsigned short) Saves the current DSP parameter settings to the specified GENSET.
    "set_preset",
        # [Deprecated] (double[2]) Configure a preset run by passing in the preset type and value. The allowed types, defined in handel_constants.h are:
        # • XIA_PRESET_FIXED_REALTIME
        # • XIA_PRESET_FIXED_LIVETIME
        # • XIA_PRESET_FIXED_TRIGGERS
        # • XIA_PRESET_FIXED_EVENTS
        # The values are defined as time in seconds, for the time based runs and counts for the other types.
        # The acquisition values preset_type and preset_value have been implemented to provide r/w access to preset run properties, and should be usedinstead.
    "get_preamp_type",
        # (unsigned short) Returns the current preamplifier type, where 0 = reset and 1 = RC feedback.
]