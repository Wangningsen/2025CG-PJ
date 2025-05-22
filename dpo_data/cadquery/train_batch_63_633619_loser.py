import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-38,-2),(-26,-29)).segment((38,3)).segment((26,29)).segment((26,13)).segment((18,13)).arc((-9,-4),(-38,-2)).assemble().finalize().extrude(200)