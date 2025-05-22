import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-30,0))
r=w0.workplane(offset=52/2).moveTo(16,33).cylinder(52,67).union(w0.sketch().segment((-83,-100),(21,-100)).segment((21,-17)).arc((57,54),(-19,14)).segment((-83,14)).close().assemble().finalize().extrude(60))