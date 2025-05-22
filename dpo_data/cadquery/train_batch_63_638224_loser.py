import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,17,0))
r=w0.workplane(offset=-34/2).cylinder(34,100)