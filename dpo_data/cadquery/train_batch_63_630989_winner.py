import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,24))
r=w0.workplane(offset=-95/2).moveTo(62,-40).cylinder(95,38).union(w0.sketch().segment((-100,-13),(-39,-13)).arc((-55,23),(-39,60)).segment((-39,62)).segment((-37,62)).arc((-9,69),(20,62)).segment((20,78)).segment((-100,78)).close().assemble().push([(-70,42)]).rect(28,4,mode='s').finalize().extrude(46))