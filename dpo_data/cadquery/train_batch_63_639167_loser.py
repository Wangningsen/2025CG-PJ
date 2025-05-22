import cadquery as cq
w0=cq.Workplane('YZ',origin=(16,0,0))
w1=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.workplane(offset=-32/2).moveTo(45.5,26.5).box(109,113,32).union(w1.workplane(offset=102/2).moveTo(-77,0).box(12,32,102))