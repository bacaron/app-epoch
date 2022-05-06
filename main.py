

from pathlib import Path
import tempfile
import numpy as np
import scipy.ndimage
import matplotlib.pyplot as plt
import mne
import json

def main():
    # Load inputs from config.json
    with open('config.json') as config_json:
        config = json.load(config_json)

    # Read the meg file
    data_file = config.pop('fif')

    # crop() the Raw data to save memory:
    raw = mne.io.read_raw_fif(data_file, verbose=False).crop(tmax=60)

    raw.pick_types(eeg=True, eog=True, stim=True).crop(tmax=60).load_data()

    report = mne.Report(title='Raw example')
    # This method also accepts a path, e.g., raw=raw_path
    report.add_raw(raw=raw, title='Raw', psd=False)  # omit PSD plot
    report.save('report_raw.html', overwrite=True)

    # # Save report
    # report.save('out_dir_report/report.html', overwrite=True)



if __name__ == '__main__':
    main()

