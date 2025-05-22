import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,27,0))
r=w0.sketch().push([(-61,12)]).circle(39).reset().face(w0.sketch().arc((29,-13),(45,-29),(63,-12)).arc((54,23),(29,-5)).segment((29,-6)).close().assemble()).finalize().extrude(-54).union(w0.workplane(offset=-36/2).moveTo(53,-4).cylinder(36,47))