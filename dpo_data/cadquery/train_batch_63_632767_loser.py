import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,63,0))
r=w0.workplane(offset=-127/2).cylinder(127,100)