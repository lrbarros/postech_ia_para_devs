import mne
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

arquivo_edf = "chb24_01.edf"
raw = mne.oi.read_raw_edf(arquivo_edf, preload=True)
raw

raw.plot(duration=10, n_channels=5)

print(raw.info)
print(raw.ch_names)
print(f"Taxa de amostragem : {raw.info['sfreq']} Hz")

data = raw.get_data()
data.shape

print("Número de canais:",data.shape[0])
print("Número de amostras:",data.shape[1])
