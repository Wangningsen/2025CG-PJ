import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-21))
w1=cq.Workplane('XY',origin=(0,0,-23))
r=w0.workplane(offset=-49/2).moveTo(44,-2).cylinder(49,11).union(w0.sketch().segment((-100,-23),(-96,-23)).arc((-97,-7),(-96,10)).segment((-100,10)).close().assemble().finalize().extrude(-4)).union(w1.sketch().segment((-5,-62),(78,-62)).segment((78,11)).segment((100,11)).segment((100,62)).segment((25,62)).segment((25,28)).segment((-5,28)).close().assemble().finalize().extrude(93))