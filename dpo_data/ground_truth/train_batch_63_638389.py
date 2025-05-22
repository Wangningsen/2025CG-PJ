import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.workplane(offset=-70/2).moveTo(45,11).cylinder(70,55).union(w0.sketch().segment((-40,-12),(-40,0)).arc((-93,-50),(-30,-12)).close().assemble().push([(-40,-37)]).circle(3,mode='s').finalize().extrude(81))