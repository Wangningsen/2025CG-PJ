import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
w1=cq.Workplane('YZ',origin=(-38,0,0))
r=w0.sketch().segment((-57,-49),(-57,-47)).arc((-52,-55),(-55,-46)).segment((-54,-46)).segment((-54,-49)).close().assemble().finalize().extrude(104).union(w0.workplane(offset=107/2).moveTo(52,8).cylinder(107,48)).union(w1.workplane(offset=58/2).moveTo(-55,-73).cylinder(58,27))