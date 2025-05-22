import cadquery as cq
w0=cq.Workplane('YZ',origin=(19,0,0))
w1=cq.Workplane('ZX',origin=(0,5,0))
r=w0.workplane(offset=-24/2).moveTo(-81,0).cylinder(24,19).union(w1.workplane(offset=95/2).moveTo(-6,-8).cylinder(95,11))