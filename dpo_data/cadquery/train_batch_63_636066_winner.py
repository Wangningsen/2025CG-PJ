import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-92,100),(-82,16)).arc((19,-5),(92,-100)).segment((92,100)).close().assemble().finalize().extrude(-200)