import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-8))
w1=cq.Workplane('XY',origin=(0,0,-46))
r=w0.sketch().segment((-65,-100),(-52,-100)).segment((-52,-21)).arc((-30,-28),(-6,-25)).arc((72,59),(-42,70)).arc((-74,36),(-65,-9)).close().assemble().finalize().extrude(-76).union(w1.workplane(offset=131/2).moveTo(-58.5,-38.5).box(35,79,131))