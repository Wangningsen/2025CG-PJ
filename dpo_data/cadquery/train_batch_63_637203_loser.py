import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-13,0))
r=w0.workplane(offset=-54/2).moveTo(-88,-32.5).box(24,45,54).union(w0.workplane(offset=80/2).moveTo(55.5,26.5).box(89,57,80))