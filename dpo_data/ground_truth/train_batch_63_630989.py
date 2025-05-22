import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
r=w0.workplane(offset=-95/2).moveTo(62,-40).cylinder(95,38).union(w0.sketch().segment((-100,-13),(-39,-13)).arc((-54,11),(-52,40)).segment((-84,40)).segment((-84,44)).segment((-50,44)).arc((-19,68),(20,62)).segment((20,78)).segment((-100,78)).close().assemble().finalize().extrude(46))