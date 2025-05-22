import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-39))
r=w0.workplane(offset=67/2).moveTo(-52,-41).cylinder(67,48).union(w0.sketch().segment((-6,53),(26,37)).segment((38,62)).segment((38,76)).segment((12,89)).close().assemble().reset().face(w0.sketch().segment((56,22),(82,9)).segment((100,46)).segment((68,62)).segment((56,37)).close().assemble()).finalize().extrude(78))