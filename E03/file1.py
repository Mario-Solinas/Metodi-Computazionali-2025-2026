import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("https://raw.githubusercontent.com/s-germani/metodi-computazionali-fisica-2025/refs/heads/main/dati/moduli_scientifici/kplr010666592-2011240104155_slc.csv")
print(df)
print(df.columns)
fig, ax = plt.subplots(figsize=(10,4))
plt.plot(df['TIME'],df['PDCSAP_FLUX'],'o',color='red', label='flux')
plt.xlabel('TIME')
plt.ylabel('PDCSAP_FLUX')
plt.title('grafico:flusso-tempo')
plt.legend(loc='upper right')
ey1=df['PDCSAP_FLUX_ERR']
plt.errorbar(df['TIME'],df['PDCSAP_FLUX'], yerr=ey1, fmt='o')

ins_ax = ax.inset_axes([.115, .78, .14, .11])
ins_ax.errorbar(
    df.loc[(df['TIME'] > 947.9) & (df['TIME'] < 948.35), 'TIME'],
    df.loc[(df['TIME'] > 947.9) & (df['TIME'] < 948.35), 'PDCSAP_FLUX'],
    yerr=df.loc[(df['TIME'] > 947.9) & (df['TIME'] < 948.35), 'PDCSAP_FLUX_ERR'],
    fmt='.',
    color='royalblue',
    label='flux zoom'
)
plt.savefig("file1.png")
plt.savefig("file2.png")
plt.show()



