import cadquery as cq
w0=cq.Workplane('YZ',origin=(-10,0,0))
w1=cq.Workplane('XY',origin=(0,0,-59))
r=w0.sketch().arc((92,59),(98,40),(94,21)).arc((100,40),(92,59)).assemble().finalize().extrude(-71).union(w0.workplane(offset=-39/2).moveTo(-79,2).cylinder(39,13)).union(w1.sketch().segment((-39,-81),(-15,-81)).arc((21,-100),(57,-81)).segment((81,-81)).segment((81,-31)).segment((57,-31)).arc((21,-12),(-15,-31)).segment((-39,-31)).close().assemble().finalize().extrude(100))