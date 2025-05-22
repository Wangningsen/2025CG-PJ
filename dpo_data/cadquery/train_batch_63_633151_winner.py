import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-53))
r=w0.workplane(offset=3/2).moveTo(54,-29).cylinder(3,46).union(w0.sketch().segment((-100,47),(30,37)).segment((32,65)).segment((28,65)).segment((28,62)).segment((11,62)).segment((11,66)).segment((-98,75)).close().assemble().finalize().extrude(106))