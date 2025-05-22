import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-47,0))
r=w0.sketch().push([(-1,70)]).circle(20).reset().face(w0.sketch().segment((-21,70),(-13,58)).segment((-6,62)).segment((-6,65)).segment((14,65)).segment((14,74)).segment((-12,74)).segment((-12,72)).segment((-15,75)).close().assemble(),mode='s').finalize().extrude(-53).union(w0.workplane(offset=147/2).moveTo(18,-86).cylinder(147,4))