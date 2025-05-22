import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-27,0))
r=w0.workplane(offset=3/2).moveTo(-75,31).cylinder(3,25).union(w0.workplane(offset=10/2).moveTo(98,-53).cylinder(10,2)).union(w0.workplane(offset=55/2).moveTo(0.5,-34).box(3,36,55))