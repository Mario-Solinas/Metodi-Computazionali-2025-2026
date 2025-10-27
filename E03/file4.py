import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Carica i dati
url = "https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv"
df = pd.read_csv(url)
print(df.head())
print(df.columns)

# Grafico completo
plt.figure(figsize=(10,5))
plt.errorbar(df['TIME'], df['PDCSAP_FLUX'], yerr=df['PDCSAP_FLUX_ERR'], fmt='o', color='red', label='flux')
plt.xlabel('TIME')
plt.ylabel('PDCSAP_FLUX')
plt.title('Grafico: flusso-tempo')
plt.legend(loc='upper right')
plt.savefig("grafico_completo.png")
plt.show()

# Selezione dell'intervallo attorno a un minimo
start = 947.9
end = 948.4
df_zoom = df.loc[(df['TIME'] >= start) & (df['TIME'] <= end)]
x = df_zoom['TIME']
y = df_zoom['PDCSAP_FLUX']
ey = df_zoom['PDCSAP_FLUX_ERR']

# Grafico zoom
plt.figure(figsize=(10,5))
plt.errorbar(x, y, yerr=ey, fmt='o', color='blue', label='zoom sul minimo')
plt.xlabel('TIME')
plt.ylabel('PDCSAP_FLUX')
plt.title('Zoom sul minimo')
plt.legend()
plt.savefig("grafico_zoom.png")
plt.show()

# Grafico completo con inset
fig, ax = plt.subplots(figsize=(10,5))
ax.errorbar(df['TIME'], df['PDCSAP_FLUX'], yerr=df['PDCSAP_FLUX_ERR'], fmt='o', color='red', label='flux')
ax.set_xlabel('TIME')
ax.set_ylabel('PDCSAP_FLUX')
ax.set_title('Grafico completo con inset')
ax.legend()

# Inserimento dell'inset
axins = inset_axes(ax, width="30%", height="30%", loc='upper right')
axins.errorbar(x, y, yerr=ey, fmt='o', color='blue')
axins.set_xlim(start, end)
axins.set_ylim(y.min()*0.99, y.max()*1.01)
axins.set_title('Zoom')

plt.savefig("grafico_inset.png")
plt.show()
