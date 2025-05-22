import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-35,-54),(35,-54)).segment((35,25)).segment((31,25)).segment((31,54)).segment((-35,54)).close().assemble().finalize().extrude(-200)