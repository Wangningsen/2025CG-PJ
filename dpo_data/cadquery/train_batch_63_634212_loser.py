import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
w1=cq.Workplane('ZX',origin=(0,-59,0))
r=w0.workplane(offset=66/2).moveTo(-19,-28).cylinder(66,47).union(w0.sketch().arc((-100,30),(-46,26),(-50,75)).segment((-58,27)).close().assemble().finalize().extrude(97)).union(w1.workplane(offset=54/2).moveTo(53,-28.5).box(94,49,54))