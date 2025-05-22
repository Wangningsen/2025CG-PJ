import cadquery as cq
w0=cq.Workplane('YZ',origin=(58,0,0))
r=w0.sketch().segment((-78,68),(-65,18)).segment((-23,28)).arc((1,30),(19,40)).segment((54,50)).segment((41,100)).segment((0,88)).arc((-23,87),(-40,75)).segment((-41,75)).close().assemble().push([(-12,59)]).circle(3,mode='s').finalize().extrude(-115).union(w0.workplane(offset=-88/2).moveTo(56,-78).cylinder(88,22))