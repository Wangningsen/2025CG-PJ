import cadquery as cq
w0=cq.Workplane('YZ',origin=(58,0,0))
r=w0.sketch().segment((-78,68),(-65,18)).segment((-19,30)).arc((-3,28),(10,37)).segment((54,50)).segment((41,100)).segment((-3,88)).arc((-19,89),(-32,82)).close().assemble().push([(-12,59)]).circle(3,mode='s').finalize().extrude(-115).union(w0.workplane(offset=-88/2).moveTo(56,-78).cylinder(88,22))