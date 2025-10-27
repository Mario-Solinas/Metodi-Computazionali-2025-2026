import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv(" https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv")
print(df)
plt.figure(figsize=(10,5))
plt.errorbar(
    df.loc[(df['TIME'] > 947.9) & (df['TIME'] < 948.35), 'TIME'],
    df.loc[(df['TIME'] > 947.9) & (df['TIME'] < 948.35), 'PDCSAP_FLUX'],
    yerr=df.loc[(df['TIME'] > 947.9) & (df['TIME'] < 948.35), 'PDCSAP_FLUX_ERR'],
    fmt='.',
    color='royalblue',
    label='flux zoom'
)
plt.savefig("file2.png")
plt.show()

