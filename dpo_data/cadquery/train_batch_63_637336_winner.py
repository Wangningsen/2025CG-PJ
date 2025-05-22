import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-57,0))
r=w0.workplane(offset=113/2).cylinder(113,100)