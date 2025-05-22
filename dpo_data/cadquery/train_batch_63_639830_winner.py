import cadquery as cq
w0=cq.Workplane('YZ',origin=(48,0,0))
w1=cq.Workplane('ZX',origin=(0,-12,0))
r=w0.workplane(offset=-95/2).moveTo(-20,0).cylinder(95,55).union(w0.workplane(offset=-69/2).moveTo(-60,-7).box(80,84,69)).union(w1.workplane(offset=112/2).moveTo(-7,20).cylinder(112,8))