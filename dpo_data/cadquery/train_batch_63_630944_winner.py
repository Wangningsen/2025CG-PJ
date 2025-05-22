import cadquery as cq
w0=cq.Workplane('YZ',origin=(-11,0,0))
w1=cq.Workplane('YZ',origin=(-32,0,0))
r=w0.sketch().segment((-37,49),(-37,67)).arc((-76,-20),(-13,49)).close().assemble().push([(63,-33)]).circle(37).circle(31,mode='s').finalize().extrude(-71).union(w0.workplane(offset=18/2).moveTo(-32,31).cylinder(18,21)).union(w0.workplane(offset=93/2).moveTo(41,-20.5).box(2,7,93)).union(w1.workplane(offset=-20/2).moveTo(24.5,-19.5).box(15,85,20))