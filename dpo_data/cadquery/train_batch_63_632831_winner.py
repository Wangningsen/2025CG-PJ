import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,6))
w1=cq.Workplane('ZX',origin=(0,-18,0))
r=w0.sketch().segment((-59,-21),(-36,-26)).segment((-49,-86)).segment((-18,-86)).arc((-6,-88),(6,-86)).segment((36,-86)).segment((36,-7)).segment((-15,-7)).segment((-14,-5)).arc((-55,88),(-57,-17)).close().assemble().finalize().extrude(-41).union(w0.workplane(offset=64/2).moveTo(-11,-47).cylinder(64,17)).union(w1.workplane(offset=-57/2).moveTo(-36,48.5).box(68,103,57))