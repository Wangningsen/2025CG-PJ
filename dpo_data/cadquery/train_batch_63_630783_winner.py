import cadquery as cq
w0=cq.Workplane('YZ',origin=(26,0,0))
r=w0.sketch().segment((-100,-50),(-82,-50)).arc((0,-96),(82,-50)).segment((100,-50)).segment((100,50)).segment((82,50)).arc((0,96),(-82,50)).segment((-100,50)).close().assemble().finalize().extrude(-52)