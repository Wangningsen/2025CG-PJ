import cadquery as cq
w0=cq.Workplane('YZ',origin=(40,0,0))
r=w0.sketch().segment((-100,-2),(-70,-2)).arc((0,-70),(70,-2)).segment((100,-2)).segment((100,2)).segment((70,2)).arc((68,10),(66,17)).arc((10,10),(17,68)).arc((-42,57),(-70,2)).segment((-100,2)).close().assemble().finalize().extrude(-80)