import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.sketch().segment((-29,53),(1,53)).arc((36,26),(70,53)).segment((100,53)).segment((100,69)).segment((70,69)).arc((36,97),(1,69)).segment((-29,69)).close().assemble().finalize().extrude(-109).union(w0.workplane(offset=13/2).moveTo(-72,-78).box(56,38,13))