import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,97,0))
r=w0.sketch().push([(61,-2)]).circle(39).reset().face(w0.sketch().segment((58,16),(59,0)).arc((61,1),(62,1)).segment((61,16)).close().assemble(),mode='s').finalize().extrude(-194).union(w0.workplane(offset=-160/2).moveTo(-82,23).cylinder(160,18))