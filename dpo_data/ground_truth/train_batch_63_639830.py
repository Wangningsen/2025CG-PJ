import cadquery as cq
w0=cq.Workplane('YZ',origin=(47,0,0))
w1=cq.Workplane('ZX',origin=(0,-33,0))
r=w0.workplane(offset=-95/2).moveTo(-20,0).cylinder(95,55).union(w0.workplane(offset=-69/2).moveTo(-68.5,-7).box(63,84,69)).union(w1.workplane(offset=133/2).moveTo(-7,19).cylinder(133,8))