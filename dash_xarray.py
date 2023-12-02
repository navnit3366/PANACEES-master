import plotly.graph_objs as go
import plotly.offline as pyo
import xarray as xr

dataset = './data/BCCAQv2+ANUSPLIN300_BNU-ESM_historical+rcp45_r1i1p1_1950-2100_tg_mean_YS.nc'
ds = xr.open_dataset(dataset)
tg_mean_subset = ds.tg_mean.loc['2020-01':'2025-01']
tg_mean = tg_mean_subset.to_dataframe().reset_index()

xmin, xmax = tg_mean['lon'].min(), tg_mean['lon'].max()
ymin, ymax = tg_mean['lat'].min(), tg_mean['lat'].max()
zmin, zmax, zmean = round(tg_mean['tg_mean'].min()), round(tg_mean['tg_mean'].max()), round(tg_mean['tg_mean'].mean())

scl = [0,"rgb(150,0,90)"],[0.125,"rgb(0, 0, 200)"],[0.25,"rgb(0, 25, 255)"],\
[0.375,"rgb(0, 152, 255)"],[0.5,"rgb(44, 255, 150)"],[0.625,"rgb(151, 255, 0)"],\
[0.75,"rgb(255, 234, 0)"],[0.875,"rgb(255, 111, 0)"],[1,"rgb(255, 0, 0)"]

data = []

for i in tg_mean['time'].unique():
    data.append(go.Scattergeo(
        lon=tg_mean['lon'][tg_mean.time == i],
        lat=tg_mean['lat'][tg_mean.time == i],
        text=tg_mean['tg_mean'][tg_mean.time == i],
        mode='markers',
        marker=dict(
            color=tg_mean['tg_mean'][tg_mean.time == i],
            colorscale=scl,
            cmax=zmax,
            cmin=zmin,
            reversescale=False,
            opacity=0.7,
            size=10,
            colorbar=dict(
                tickvals=[zmin, zmean, zmax],
                tickmode='array',
                thickness=20,
                titleside="left",
                outlinecolor="rgba(68, 68, 68, 0)",
                ticks="outside",
                ticksuffix=" Kelvin"))
        )
    )

steps = []
for i in range(len(data)):
    step = dict(method='restyle',
                args=['visible', [False] * len(data)],
                label='{}'.format(i + 2020))
    step['args'][1][i] = True
    steps.append(step)

sliders = [dict(active=10, pad={'t': 50, 'b':10}, currentvalue={'prefix': 'Year: '}, steps=steps)]

layout = dict(title='BCCAQv2 Mean Temperature',
              sliders=sliders,
              legend=dict(orientation='h'),
              geo=dict(
                  scope='north america',
                  lonaxis=dict(
                      showgrid=True,
                      gridwidth=0.5,
                      range=[xmin-5, xmax+5],
                      dtick=5
                  ),
                  lataxis=dict(
                      showgrid=True,
                      gridwidth=0.5,
                      range=[ymin-5, ymax+5],
                      dtick=5
                  ),
              )
        )

fig = dict(data=data, layout=layout)
pyo.plot(fig)

