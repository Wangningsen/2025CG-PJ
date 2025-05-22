import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
r=w0.workplane(offset=33/2).cylinder(33,25).union(w0.workplane(offset=33/2).cylinder(33,100))