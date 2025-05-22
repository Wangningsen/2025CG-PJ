import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.workplane(offset=56/2).moveTo(65,-30).cylinder(56,35).union(w0.sketch().push([(-71,36)]).circle(29).reset().face(w0.sketch().segment((-84,36),(-62,22)).segment((-49,41)).segment((-71,56)).close().assemble(),mode='s').push([(-26,36)]).circle(6).circle(2,mode='s').finalize().extrude(87))