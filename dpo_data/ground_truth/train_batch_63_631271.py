import cadquery as cq
w0=cq.Workplane('YZ',origin=(14,0,0))
r=w0.sketch().segment((77,32),(81,13)).arc((84,11),(82,8)).segment((92,-38)).segment((100,-36)).segment((86,33)).close().assemble().push([(89,-2)]).circle(3,mode='s').finalize().extrude(-46).union(w0.workplane(offset=17/2).moveTo(-44,26).box(112,24,17))