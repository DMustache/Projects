import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.patches import PathPatch
from mpl_toolkits.basemap import Basemap

m = Basemap(resolution='c', projection='kav7', lat_0=0., lon_0=0.)
n_graticules = 18
parallels = np.arange(-80., 90, n_graticules)
meridians = np.arange(0., 360., n_graticules)
lw = 1
dashes = [5,7] # 5 dots, 7 spaces... repeat
graticules_color = 'grey'

fig1 = plt.figure(figsize=(16,20))
fig1.patch.set_facecolor('#e6e8ec')
ax = fig1.add_axes([0.1,0.1,0.8,0.8])

m.drawmapboundary(color='white', 
                  linewidth=0.0, 
                  fill_color='white')
m.drawparallels(parallels, 
                linewidth=lw, 
                dashes=dashes, 
                color=graticules_color)
m.drawmeridians(meridians, 
                linewidth=lw, 
                dashes=dashes, 
                color=graticules_color)
m.drawcoastlines(linewidth=0)
m.fillcontinents('black', 
                 lake_color='white')
m.drawcountries(linewidth=1, 
                linestyle='solid', 
                color='white', 
                zorder=30)

title = plt.title('World map (Kavrayskiy 7)', 
                  fontsize=20) 
title.set_y(1.03)

m.readshapefile('shapefiles/ne_110m_populated_places/ne_110m_populated_places', 
                name='populated_places', 
                drawbounds=False, 
                color='none')

populations = [r['POP2000'] for r in m.populated_places_info]
lats = [r['LATITUDE'] for r in m.populated_places_info]
lons = [r['LONGITUDE'] for r in m.populated_places_info]
x1, y1 = m(lons, lats)
m.scatter(x1, y1, 
          s=np.array(populations)*0.05, 
          marker="o", 
          color='#32caf6',
          zorder=10, 
          alpha=0.8)

m.readshapefile('shapefiles/tectonicplates-master/PB2002_plates', 
                name='tectonic_plates', 
                drawbounds=True, 
                color='red')

for info, shape in zip(m.tectonic_plates_info, 
                       m.tectonic_plates):

    if info['PlateName'] == "Australia":
        x, y = zip(*shape) 
        m.plot(x, y, marker=None, color='b')

        
patches = []
for info, shape in zip(m.tectonic_plates_info, 
                       m.tectonic_plates):

    if info['PlateName'] == "Australia":
        patches.append(Polygon(np.array(shape), True))
        
ax.add_collection(PatchCollection(patches, 
                                  facecolor='#32caf6', 
                                  edgecolor='none', 
                                  linewidths=1., 
                                  alpha=0.5,
                                  zorder=1))