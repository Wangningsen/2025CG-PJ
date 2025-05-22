import cadquery as cq
w0=cq.Workplane('YZ',origin=(15,0,0))
r=w0.sketch().segment((77,32),(81,14)).arc((83,12),(82,9)).segment((92,-38)).segment((100,-36)).segment((86,33)).close().assemble().push([(89,-2)]).circle(3,mode='s').finalize().extrude(-47).union(w0.workplane(offset=16/2).moveTo(-44,26).box(112,24,16))