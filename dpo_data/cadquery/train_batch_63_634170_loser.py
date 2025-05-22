import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-57,0))
r=w0.workplane(offset=-43/2).cylinder(43,91).union(w0.sketch().arc((-51,3),(-34,23),(-51,45)).close().assemble().finalize().extrude(70)).union(w0.workplane(offset=157/2).moveTo(-64,22.5).box(26,63,157))