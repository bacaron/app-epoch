# Epochs objects are a data structure for representing and analyzing equal-duration chunks of the EEG/MEG signal. Epochs are
# most often used to represent data that is time-locked to repeated experimental events (such as stimulus onsets or subject button presses),
import mne
import json
import os
import matplotlib.pyplot as plt

# Current path
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


def epoch(raw, events, tmin, tmax):


    epochs = mne.Epochs(raw, events, tmin=tmin, tmax=tmax)

    epochs.plot(n_epochs=10)

    # == SAVE FILE ==
    epochs.save(os.path.join('out_dir', 'meg-epo.fif'))

    # == FIGURES ==
    plt.figure()
    epochs.plot()
    plt.savefig(os.path.join('out_figs', 'epochs_plot.png'))

    return epochs


def main():
    # Load inputs from config.json
    with open('config.json') as config_json:
        config = json.load(config_json)

    # Read the meg file
    data_file = config.pop('fif')

    # Read the event time
    tmin = config.pop('t_min')
    tmax = config.pop('t_max')

    # crop() the Raw data to save memory:
    raw = mne.io.read_raw_fif(data_file, verbose=False).crop(tmax=60)

    if 'events' in config.keys():
        events_file = config.pop('events')
        events = mne.read_events(events_file)
    else:
        # extract an events array from Raw objects using mne.find_events():
        # reading experimental events from a “STIM” channel;
        events = mne.find_events(raw, stim_channel='STI 014')

    ## Build epochs parameters
    epochs_params = dict(tmin=tmin, tmax=tmax)

    epochs = epoch(raw, events, **epochs_params)



if __name__ == '__main__':
    main()