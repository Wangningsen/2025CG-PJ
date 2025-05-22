import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().arc((-9,-2),(9,0),(-9,2)).arc((-7,0),(-9,-2)).assemble().finalize().extrude(200)