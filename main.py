#Epochs objects are a data structure for representing and analyzing equal-duration chunks of the EEG/MEG signal. Epochs are
# most often used to represent data that is time-locked to repeated experimental events (such as stimulus onsets or subject button presses),
import mne
import json
import os

sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = os.path.join(sample_data_folder, 'MEG', 'sample',
                                    'sample_audvis_raw.fif')
#crop() the Raw data to save memory:
raw = mne.io.read_raw_fif(sample_data_raw_file, verbose=False).crop(tmax=60)

#extract an events array from Raw objects using mne.find_events():
events = mne.find_events(raw, stim_channel='STI 014')

epochs = mne.Epochs(raw, events, tmin=-0.3, tmax=0.7)
print(epochs)

def main():


    # Load inputs from config.json
    with open('config.json') as config_json:
        config = json.load(config_json)

    # Read the meg file
    data_file = config.pop('fif')
    raw = mne.io.read_raw_fif(data_file, allow_maxshield=True)




if __name__ == '__main__':
    main()