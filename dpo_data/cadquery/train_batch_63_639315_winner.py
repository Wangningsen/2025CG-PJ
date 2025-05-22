import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
w1=cq.Workplane('XY',origin=(0,0,41))
r=w0.sketch().arc((92,21),(100,38),(92,59)).segment((92,54)).arc((98,38),(92,23)).close().assemble().finalize().extrude(-71).union(w0.workplane(offset=-39/2).moveTo(-80,2).cylinder(39,12)).union(w1.sketch().segment((-39,-81),(-15,-81)).arc((21,-100),(57,-81)).segment((81,-81)).segment((81,-31)).segment((57,-31)).arc((21,-12),(-15,-31)).segment((-39,-31)).close().assemble().finalize().extrude(-100))