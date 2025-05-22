import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-43,0))
r=w0.workplane(offset=56/2).moveTo(65,-30).cylinder(56,35).union(w0.sketch().push([(-71,36)]).circle(29).reset().face(w0.sketch().segment((-84,38),(-62,22)).segment((-51,38)).segment((-73,55)).close().assemble(),mode='s').push([(-26,37)]).circle(5).finalize().extrude(87))