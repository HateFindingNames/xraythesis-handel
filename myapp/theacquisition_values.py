acquisition_values = {
    # Filter
    "parset": "The current PARSET.",
    "genset": "The current GENSET.",
    "fippi": "The current FiPPI.",
    "clock_speed": "The digitizing clock in MHz. This value will be rounded to the nearest setting supported by the hardware, which is either DSPCLK, DSPCLK/2, DSPCLK/4 or DSPCLK/8. Not all selections are available on all hardware.,",
    "energy_gap_time": "The gap time of the energy filter, specified in microseconds.",
    "trigger_peak_time": "The peaking time of the trigger filter, specified in microseconds.",
    "trigger_gap_time": "The gap time of the trigger filter, specified in microseconds.",
    "baseline_length": "The number of samples averaged together for the baseline filter.",
    "trigger_threshold": "Trigger filter threshold in arbitrary units.",
    "baseline_threshold": "Baseline filter threshold in arbitrary units.",
    "energy_threshold": "Energy filter threshold in arbitrary units.",
    "peak_interval_offset": "The peak interval specified as an offset from the peaking time and gap time, specified in microseconds. Effectively sets PEAKINT= SLOWLEN + SLOWGAP + peak_interval_offset. Added in v1.2.2.",
    "peak_sample_offset": "Energy filter sampling time measured backward from the peaking time and gap time, specified in μs.Effectively sets PEAKSAM= SLOWLEN + SLOWGAP - peak_sample_offset. Added in v1.2.2.",
    "max_width": "The value of MAXWIDTH, specified in microseconds.",
    "peak_mode": "The value of PEAKINT. Sets the value of PEAKMODE to “Peak-Sensing” (PEAKMODE=0) or “Peak-Sampling” (PEAKMODE=1). Added in v1.2.2.",
    "peak_interval": "[Deprecated] The value of PEAKINT, specified in microseconds. Deprecated in v1.2.2, use peak_interval_offset instead.",
    "peak_sample": "[Deprecated] The value of PEAKSAM, specified in μs. Deprecated in v1.2.2, use peak_sample_offset instead.",
    # Detector
    "polarity": "The detector preamplifier polarity, where the allowed values are 0 = negative and 1 = positive.",
    "preamp_value": "Either the reset interval, for reset-type preamplifiers, or the decay time, for RC feedback-type detectors. The reset interval is specified in microseconds and the decay time is specified in terms of the digitization clock period.",
    # Gain
    "gain": "The base gain in arbitrary units.",
    "gain_trim": "Adjusts the base gain per PARSET, specified in arbitrary units.",
    # Preset Run Control
    "preset_type": "Set the preset run type. See handel_constants.h for the constants that can be used. The supported preset type for microDXP are:\n* XIA_PRESET_FIXED_REALTIME\n* XIA_PRESET_FIXED_LIVETIME\n* XIA_PRESET_FIXED_TRIGGERS\n* XIA_PRESET_FIXED_EVENTS",
    "preset_value": "When a preset run type other then XIA_PRESET_NONE is set, this value is either the number of counts or a time (specfied in seconds). MCA Data Acquisition",
    "number_mca_channels": "The number of bins in the MCA spectrum, defined in bins.",
    "mca_bin_width": "Width of an individual bin in the MCA, specified in eV.",
    "bytes_per_bin": "The number of bytes returned per bin when reading out the MCA spectrum. Can be either 1, 2 or 3 bytes.",
    "adc_trace_wait": "When acquiring an ADC trace for readout, the amount of time to wait between ADC samples, specified in microseconds.",
    "auto_adjust_offset": "Whether the DAC will remain static until next power cycle or re-adjusted whenever analog gain or other settings are changed. (0: static, 1: auto adjusted).",
    # SCA Data Acquisition
    "number_of_scas": "Sets the number of SCAs. **sca\{N\}_[lo|hi]** The SCA limit (low or high) for the requested SCA, N, specified as a bin number. N ranges from 0 to \"number_of_scas\" - 1.",
}