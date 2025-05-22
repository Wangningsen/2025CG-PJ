import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
r=w0.workplane(offset=-39/2).cylinder(39,100)