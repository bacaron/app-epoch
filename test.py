#!/usr/local/bin/python3

import mne
import json
import os


def main():


    # Load inputs from config.json
    with open('config.json') as config_json:
        config = json.load(config_json)

    # Read the meg file
    data_file = config.pop('fif')
    raw = mne.io.read_raw_fif(data_file, allow_maxshield=True)




if __name__ == '__main__':
    main()