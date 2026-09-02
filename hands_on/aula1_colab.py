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

raw_filtrado = raw.copy().filter(0.5, 40)
raw_filtrado.plot(duration = 10, n_channels = 5)

data_filtrado = raw_filtrado.get_data()
data_filtrado.shape

with open ("chb24-summary.txt", "r") as f:
    conteudo = f.readlines()

for linha in conteudo[:40]:
    print(linha.strip())

seizure_intervals_sec = [
	(480,505),
	(2451,2476)
    ]
sfreq = raw.info["sfreq"]

canal_idx = 0
signal = data_filtrado[canal_idx]

time = np.arange(len(signal)) / sfreq

plt.figure(figsize=(16,4))
plt.plot(time, signal, linewidth=0.7)

for i,(start,end) in enumerate(seizure_intervals_sec):
	plt.axvspan(start, end, color="red", alpha=0,25
	label="Crise", if i==0 else None)

plt.xlabel("Tempo (s)")
plt.ylabel("Amplitude")
plt.title("EEG com intervalos de crise destacados")
plt.legend()
plt.show()
