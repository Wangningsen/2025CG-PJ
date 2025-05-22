import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-78,0))
r=w0.workplane(offset=156/2).cylinder(156,100)