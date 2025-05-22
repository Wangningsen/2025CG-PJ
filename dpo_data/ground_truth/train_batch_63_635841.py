import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,57))
r=w0.sketch().arc((86,-15),(100,16),(86,46)).close().assemble().finalize().extrude(-115).union(w0.workplane(offset=-52/2).moveTo(-79,-25).cylinder(52,21))