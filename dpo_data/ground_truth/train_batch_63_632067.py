import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
r=w0.workplane(offset=77/2).cylinder(77,100)