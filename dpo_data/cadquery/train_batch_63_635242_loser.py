import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,79,0))
r=w0.workplane(offset=-158/2).cylinder(158,100)