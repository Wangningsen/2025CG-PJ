import cadquery as cq
w0=cq.Workplane('YZ',origin=(-99,0,0))
r=w0.sketch().arc((-10,70),(-78,-27),(21,-99)).arc((-2,-1),(79,71)).arc((50,88),(20,100)).segment((13,73)).close().assemble().push([(-1,58)]).circle(7,mode='s').finalize().extrude(22).union(w0.workplane(offset=198/2).moveTo(8,-14).cylinder(198,4))