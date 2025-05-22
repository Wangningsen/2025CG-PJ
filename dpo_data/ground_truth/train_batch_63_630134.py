import cadquery as cq
w0=cq.Workplane('YZ',origin=(57,0,0))
r=w0.sketch().segment((-78,68),(-65,18)).segment((-24,28)).arc((-19,31),(-15,28)).arc((0,29),(12,38)).segment((54,50)).segment((41,100)).segment((-1,88)).arc((-21,88),(-35,79)).close().assemble().push([(-12,59)]).circle(3,mode='s').finalize().extrude(-115).union(w0.workplane(offset=-87/2).moveTo(56,-78).cylinder(87,22))