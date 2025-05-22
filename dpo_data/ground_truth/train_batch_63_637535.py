import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,19,0))
w1=cq.Workplane('ZX',origin=(0,-17,0))
r=w0.workplane(offset=-38/2).moveTo(-37,-64).cylinder(38,3).union(w1.sketch().arc((18,23),(-100,1),(20,8)).segment((100,8)).segment((100,23)).close().assemble().finalize().extrude(11))