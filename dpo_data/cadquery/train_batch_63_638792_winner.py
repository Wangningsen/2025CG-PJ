import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-36,0))
w1=cq.Workplane('YZ',origin=(-28,0,0))
r=w0.workplane(offset=72/2).moveTo(4,52).cylinder(72,48).union(w1.workplane(offset=-72/2).moveTo(-26,-49).cylinder(72,3))