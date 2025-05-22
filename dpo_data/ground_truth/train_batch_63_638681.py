import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-25,0))
r=w0.workplane(offset=-75/2).moveTo(14,9).cylinder(75,27).union(w0.sketch().push([(-27,-22)]).circle(14).reset().face(w0.sketch().segment((-31,-21),(-30,-21)).arc((-26,-25),(-26,-19)).segment((-26,-16)).segment((-31,-16)).close().assemble(),mode='s').finalize().extrude(125))