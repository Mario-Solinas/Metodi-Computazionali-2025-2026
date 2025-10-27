home/mario/MCF/E03/file3.py", line 7, in <module>
    df = pd.read_csv(url)
         ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 948, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 611, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 1448, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 1705, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/common.py", line 718, in get_handle
    ioargs = _get_filepath_or_buffer(
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/common.py", line 372, in _get_filepath_or_buffer
    with urlopen(req_info) as req:
         ^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/common.py", line 274, in urlopen
    return urllib.request.urlopen(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 215, in urlopen
    return opener.open(url, data, timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 521, in open
    response = meth(req, response)
               ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 630, in http_response
    response = self.parent.error(
               ^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 559, in error
    return self._call_chain(*args)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 492, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 639, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found File "/home/mario/MCF/E03/file3.py", line 7, in <module>
    df = pd.read_csv(url)
         ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 948, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 611, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 1448, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 1705, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/common.py", line 718, in get_handle
    ioargs = _get_filepath_or_buffer(
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/common.py", line 372, in _get_filepath_or_buffer
    with urlopen(req_info) as req:
         ^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/common.py", line 274, in urlopen
    return urllib.request.urlopen(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 215, in urlopen
    return opener.open(url, data, timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 521, in open
    response = meth(req, response)
               ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 630, in http_response
    response = self.parent.error(
               ^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 559, in error
    return self._call_chain(*args)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 492, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 639, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Found File "/home/mario/MCF/E03/file3.py", line 7, in <module>
    df = pd.read_csv(url)
         ^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 948, in read_csv
    return _read(filepath_or_buffer, kwds)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 611, in _read
    parser = TextFileReader(filepath_or_buffer, **kwds)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 1448, in __init__
    self._engine = self._make_engine(f, self.engine)
                   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/parsers/readers.py", line 1705, in _make_engine
    self.handles = get_handle(
                   ^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/common.py", line 718, in get_handle
    ioargs = _get_filepath_or_buffer(
             ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/common.py", line 372, in _get_filepath_or_buffer
    with urlopen(req_info) as req:
         ^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3/dist-packages/pandas/io/common.py", line 274, in urlopen
    return urllib.request.urlopen(*args, **kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 215, in urlopen
    return opener.open(url, data, timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 521, in open
    response = meth(req, response)
               ^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 630, in http_response
    response = self.parent.error(
               ^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 559, in error
    return self._call_chain(*args)
           ^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 492, in _call_chain
    result = func(*args)
             ^^^^^^^^^^^
  File "/usr/lib/python3.12/urllib/request.py", line 639, in http_error_default
    raise HTTPError(req.full_url, code, msg, hdrs, fp)
urllib.error.HTTPError: HTTP Error 404: Not Foundimport pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

# Carica i dati
url = ""
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
df_zoom = df.loc[(df['TIME'] >= start) & (df['TIME'] <= end)]  # correzione & con parentesi
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
axins = inset_axes(ax, width="30%", height="30%", loc='upper right')  # dimensione e posizione
axins.errorbar(x, y, yerr=ey, fmt='o', color='blue')
axins.set_xlim(start, end)
axins.set_ylim(y.min()*0.99, y.max()*1.01)  # margine piccolo
axins.set_title('Zoom')

plt.savefig("grafico_inset.png")
plt.show()
