import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-87,0))
r=w0.workplane(offset=174/2).cylinder(174,100)