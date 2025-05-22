import cadquery as cq
w0=cq.Workplane('YZ',origin=(10,0,0))
r=w0.workplane(offset=-57/2).moveTo(32,31.5).box(6,91,57).union(w0.workplane(offset=-35/2).moveTo(-60,-37).cylinder(35,40)).union(w0.sketch().arc((95,-62),(100,-45),(95,-28)).close().assemble().finalize().extrude(37))