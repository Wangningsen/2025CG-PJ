import cadquery as cq
w0=cq.Workplane('YZ',origin=(48,0,0))
w1=cq.Workplane('ZX',origin=(0,-47,0))
r=w0.workplane(offset=-95/2).moveTo(-19,0).cylinder(95,55).union(w0.workplane(offset=-69/2).moveTo(-66.5,-7).box(67,84,69)).union(w1.sketch().push([(-7,19)]).circle(9).circle(8,mode='s').finalize().extrude(147))