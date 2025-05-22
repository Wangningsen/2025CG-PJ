import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-13))
w1=cq.Workplane('XY',origin=(0,0,-4))
r=w0.workplane(offset=46/2).moveTo(-28,71).cylinder(46,29).union(w1.sketch().segment((-1,-100),(57,-100)).segment((57,-12)).segment((43,-12)).arc((-19,5),(-1,-58)).close().assemble().finalize().extrude(-29))