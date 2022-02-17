import librosa
import numpy as np


def get_tempo(y):
    """Get tempo of the audio file (in BPM).

    Args:
        y (np.ndArray): audio time series

    Returns:
        dict: tempo key-value pair
    """

    tempo, _ = librosa.beat.beat_track(y)
    return {"tempo": tempo}


def get_hpss(y):
    """Get harmonics and perceptruals of the audio file.

    Args:
        y (np.ndArray): audio time series

    Returns:
        dict: means and variances
    """

    y_harm, y_perc = librosa.effects.hpss(y)

    results = {
        "harm_mean": np.mean(y_harm),
        "harm_var": np.var(y_harm),
        "perc_mean": np.mean(y_perc),
        "perc_var": np.var(y_perc),
    }

    return results


def get_cens(y, sr):
    """Get Chromatics energy normalized features of the audio file.

    Args:
        y (np.ndArray): audio time series
        sr (int): sampling rate

    Returns:
        dict: means and variances for each features(12)
    """

    cens = librosa.feature.chroma_cens(y, sr=sr)
    cens_mean_labels = [f"cen{i}_mean" for i in range(1, len(cens)+1)]
    cens_var_labels = [f"cen{i}_var" for i in range(1, len(cens)+1)]
    cens_means = [np.mean(cen) for cen in cens]
    cens_vars = [np.var(cen) for cen in cens]
    labels = cens_mean_labels + cens_var_labels
    values = cens_means + cens_vars
    results = dict(zip(labels, values))

    return results


def get_stfts(y, sr):
    """Get normalized energy of the audio file

    Args:
        y (np.ndArray): audio time series
        sr (int): sampling rate

    Returns:
        dict: means and variances for each features(12)
    """

    stfts = librosa.feature.chroma_stft(y, sr=sr)
    stfts_mean_labels = [f"stft{i}_mean" for i in range(1, len(stfts)+1)]
    stfts_var_labels = [f"stft{i}_var" for i in range(1, len(stfts)+1)]
    stfts_means = [np.mean(stft) for stft in stfts]
    stfts_vars = [np.var(stft) for stft in stfts]
    labels = stfts_mean_labels + stfts_var_labels
    values = stfts_means + stfts_vars
    results = dict(zip(labels, values))

    return results


def get_zero_crossing_rate(y):
    """Get the rate at which the signal changes from positive to negative.

    Args:
        y (np.ndArray): audio time series

    Returns:
        dict: zero_crossing_rate
    """

    return {"zero_crossings": sum(librosa.zero_crossings(y, pad=False))}


def get_spectral_features(y, sr):
    """Get spectral features of the audio file.

    Args:
        y (np.ndArray): audio time series
        sr (int): sampling rate

    Returns:
        dict: means and variances for each feature
    """

    spectral_centroids = librosa.feature.spectral_centroid(y, sr=sr)[0]
    spectral_rolloff = librosa.feature.spectral_rolloff(y, sr=sr)[0]
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y, sr=sr)[0]
    spectral_contrast = librosa.feature.spectral_contrast(y, sr=sr)[0]

    results = {
        "centroids_mean": np.mean(spectral_centroids),
        "centroids_var": np.var(spectral_centroids),
        "rolloff_mean": np.mean(spectral_rolloff),
        "rolloff_var": np.var(spectral_rolloff),
        "bandwidth_mean": np.mean(spectral_bandwidth),
        "bandwidth_var": np.var(spectral_bandwidth),
        "contrast_mean": np.mean(spectral_contrast),
        "contrast_var": np.var(spectral_contrast),
        }
    return results


def get_rms(y):
    """Get tempo of the audio file (in BPM).

    Args:
        y (np.ndArray): audio time series

    Returns:
        dict: tempo key-value pair
    """

    rms = librosa.feature.rms(y)
    results = {
        "rms_mean": np.mean(rms),
        "rms_var": np.var(rms),
    }
    return results


def get_mfccs(y, sr):
    """Get tempo of the audio file (in BPM).

    Args:
        y (np.ndArray): audio time series
        sr (int): sampling rate

    Returns:
        dict: tempo key-value pair
    """

    mfccs = librosa.feature.mfcc(y, sr=sr)
    mfccs_mean_labels = [f"mfcc{i}_mean" for i in range(1, len(mfccs)+1)]
    mfccs_var_labels = [f"mfcc{i}_var" for i in range(1, len(mfccs)+1)]
    mfccs_means = [np.mean(mfcc) for mfcc in mfccs]
    mfccs_vars = [np.var(mfcc) for mfcc in mfccs]
    labels = mfccs_mean_labels + mfccs_var_labels
    values = mfccs_means + mfccs_vars
    results = dict(zip(labels, values))
    return results


def extract_features(y, sr):
    """Get tempo of the audio file (in BPM).

    Args:
        y (np.ndArray): audio time series
        sr (int): sampling rate

    Returns:
        dict: tempo key-value pair
    """

    features_dict = {}
    features = [
        get_tempo(y),
        get_hpss(y),
        get_rms(y),
        get_zero_crossing_rate(y),
        get_spectral_features(y, sr),
        get_stfts(y, sr),
        get_cens(y, sr)
    ]

    for f in features:
        features_dict.update(f)

    return features_dict

# TODO: Création de deux fonctions différentes pour : 
#   1) calcul des mean_label et mean_values (exemple : get_cens())
#   2) création de result avec np.mean() et np.var() (exemple : get_spectral_features())