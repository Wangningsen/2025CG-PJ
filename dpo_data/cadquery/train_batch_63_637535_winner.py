import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-17,0))
w1=cq.Workplane('ZX',origin=(0,-19,0))
r=w0.sketch().arc((13,34),(-99,-2),(20,8)).segment((100,8)).segment((100,23)).segment((13,23)).close().assemble().finalize().extrude(11).union(w1.workplane(offset=38/2).moveTo(-37,-64).cylinder(38,3))