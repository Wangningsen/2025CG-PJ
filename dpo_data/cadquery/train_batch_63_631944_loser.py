import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-87))
r=w0.workplane(offset=-13/2).moveTo(-17,-11).box(14,130,13).union(w0.sketch().segment((-67,60),(32,60)).arc((-17,76),(-67,60)).assemble().reset().face(w0.sketch().arc((55,-47),(67,-7),(55,34)).close().assemble()).finalize().extrude(187))