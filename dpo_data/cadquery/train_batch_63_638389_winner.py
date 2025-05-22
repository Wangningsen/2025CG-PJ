import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.workplane(offset=-69/2).moveTo(45,11).cylinder(69,55).union(w0.sketch().segment((-41,-12),(-41,0)).arc((-92,-52),(-31,-12)).close().assemble().push([(-40,-37)]).circle(3,mode='s').finalize().extrude(82))