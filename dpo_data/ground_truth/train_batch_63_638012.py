import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-33))
w1=cq.Workplane('XY',origin=(0,0,-13))
r=w0.sketch().segment((-1,-100),(57,-100)).segment((57,-12)).segment((43,-12)).arc((-19,5),(-1,-58)).close().assemble().finalize().extrude(29).union(w1.sketch().segment((-57,62),(-56,62)).arc((1,75),(-57,75)).close().assemble().finalize().extrude(46))