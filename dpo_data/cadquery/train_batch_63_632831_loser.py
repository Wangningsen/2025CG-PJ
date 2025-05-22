import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
w1=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.sketch().arc((-35,-25),(-45,-70),(-6,-86)).segment((36,-86)).segment((36,-7)).segment((-4,-7)).arc((-62,86),(-35,-22)).close().assemble().finalize().extrude(41).union(w0.workplane(offset=105/2).moveTo(-11,-47).cylinder(105,17)).union(w1.workplane(offset=-57/2).moveTo(-36,48.5).box(68,103,57))