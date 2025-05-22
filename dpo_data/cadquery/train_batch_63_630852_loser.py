import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-19,0))
r=w0.workplane(offset=20/2).moveTo(-37,-27.5).box(126,131,20).union(w0.workplane(offset=39/2).moveTo(45,55).box(110,76,39))