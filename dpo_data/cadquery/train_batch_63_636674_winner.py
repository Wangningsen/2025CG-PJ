import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-49,-9),(1,-9)).segment((1,-83)).arc((17,-69),(29,-50)).segment((49,-50)).segment((49,21)).segment((29,21)).arc((26,26),(22,32)).segment((22,83)).segment((-49,83)).close().assemble().finalize().extrude(-200)