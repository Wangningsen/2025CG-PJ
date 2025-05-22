import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-16,-15),(-16,-1)).segment((-5,-1)).segment((-5,15)).segment((16,15)).segment((16,-1)).close().assemble().finalize().extrude(-200)