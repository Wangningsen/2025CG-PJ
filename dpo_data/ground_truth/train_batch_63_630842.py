import cadquery as cq
w0=cq.Workplane('YZ',origin=(97,0,0))
r=w0.sketch().segment((-100,-19),(-58,-83)).segment((100,23)).segment((53,83)).close().assemble().finalize().extrude(-194)