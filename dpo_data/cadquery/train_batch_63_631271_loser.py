import cadquery as cq
w0=cq.Workplane('YZ',origin=(15,0,0))
r=w0.sketch().segment((77,32),(83,6)).segment((88,6)).segment((88,3)).segment((84,3)).segment((92,-38)).segment((100,-36)).segment((86,33)).close().assemble().finalize().extrude(-47).union(w0.workplane(offset=16/2).moveTo(-44,26).box(112,24,16))