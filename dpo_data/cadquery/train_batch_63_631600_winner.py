import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-40,-51),(-40,51)).arc((-65,0),(-40,-51)).assemble().reset().face(w0.sketch().arc((40,-51),(65,0),(40,51)).close().assemble()).finalize().extrude(-121).union(w0.workplane(offset=79/2).cylinder(79,26))