import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
r=w0.workplane(offset=-94/2).moveTo(62,-40).cylinder(94,38).union(w0.sketch().segment((-100,-13),(-40,-13)).arc((-54,10),(-53,37)).segment((-84,37)).segment((-84,44)).segment((-49,44)).arc((-18,68),(20,63)).segment((20,78)).segment((-100,78)).close().assemble().finalize().extrude(46))