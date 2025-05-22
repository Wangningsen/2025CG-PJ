import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-38,0))
w1=cq.Workplane('XY',origin=(0,0,6))
r=w0.workplane(offset=66/2).moveTo(-19,-28).cylinder(66,47).union(w0.sketch().arc((-100,30),(-49,23),(-50,75)).segment((-59,23)).close().assemble().finalize().extrude(97)).union(w1.workplane(offset=94/2).moveTo(-28.5,-32).box(49,54,94))