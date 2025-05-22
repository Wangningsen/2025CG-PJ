import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-7,-5),(7,-5)).arc((-1,-1),(-7,5)).close().assemble().finalize().extrude(-200)