import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-37))
w1=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().segment((-26,14),(-20,14)).arc((13,-19),(45,14)).segment((100,14)).segment((100,51)).segment((42,51)).segment((58,24)).segment((34,11)).segment((16,41)).segment((34,51)).segment((-26,51)).close().assemble().finalize().extrude(-18).union(w1.workplane(offset=98/2).moveTo(-53.5,0).box(93,182,98))