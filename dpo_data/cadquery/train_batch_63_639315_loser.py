import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
w1=cq.Workplane('XY',origin=(0,0,41))
r=w0.sketch().segment((92,59),(99,28)).arc((99,46),(92,59)).assemble().finalize().extrude(-71).union(w0.workplane(offset=-39/2).moveTo(-80,3).cylinder(39,14)).union(w1.sketch().segment((-39,-81),(-15,-81)).arc((21,-100),(57,-81)).segment((81,-81)).segment((81,-31)).segment((57,-31)).arc((21,-12),(-15,-31)).segment((-39,-31)).close().assemble().finalize().extrude(-100))