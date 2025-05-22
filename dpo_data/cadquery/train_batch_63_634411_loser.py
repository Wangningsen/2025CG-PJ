import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-95,0))
r=w0.workplane(offset=190/2).cylinder(190,100)