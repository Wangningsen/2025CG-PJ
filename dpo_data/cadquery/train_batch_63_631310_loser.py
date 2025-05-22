import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-22,-26),(22,-26)).arc((-4,-3),(-22,26)).close().assemble().finalize().extrude(200)