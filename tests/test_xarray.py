import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import xarray as xr
airtemps = xr.tutorial.open_dataset('air_temperature')
airtemps
air = airtemps.air - 273.15
air.attrs = airtemps.air.attrs
air.attrs['units'] = 'deg C'
air1d = air.isel(lat=10, lon=10)
air1d.plot()
plt.show()

air1d.attrs
air1d[:200].plot.line('b-^')
air1d[:200].plot.line(color='purple', marker='o')
fig, axes = plt.subplots(ncols=2)
axes
air1d.plot(ax=axes[0])
air1d.plot.hist(ax=axes[1])
plt.tight_layout()
plt.draw()
air1d.plot(aspect=2, size=3)

plt.tight_layout()
plt.show()

t = air.isel(time=slice(0, 365 * 4, 250))
g_simple = t.plot(x='lon', y='lat', col='time', col_wrap=3)
plt.show()
