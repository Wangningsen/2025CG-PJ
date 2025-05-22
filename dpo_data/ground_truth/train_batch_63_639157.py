import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-4,0))
w1=cq.Workplane('XY',origin=(0,0,-46))
r=w0.sketch().segment((-100,-71),(-13,-71)).segment((-13,-47)).arc((68,25),(-31,68)).segment((-100,68)).close().assemble().finalize().extrude(35).union(w1.workplane(offset=146/2).moveTo(-58,-10).cylinder(146,21))