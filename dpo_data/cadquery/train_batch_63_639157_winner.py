import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-46))
w1=cq.Workplane('ZX',origin=(0,31,0))
r=w0.workplane(offset=146/2).moveTo(-58,-10).cylinder(146,21).union(w1.sketch().segment((-100,-71),(-13,-71)).segment((-13,-47)).arc((69,16),(-26,71)).segment((-26,68)).segment((-100,68)).close().assemble().finalize().extrude(-35))