import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
w1=cq.Workplane('YZ',origin=(-25,0,0))
r=w0.sketch().segment((26,6),(30,6)).segment((30,-26)).segment((35,-43)).arc((44,-29),(53,-18)).arc((92,14),(39,14)).arc((33,10),(26,6)).assemble().finalize().extrude(-67).union(w0.workplane(offset=-5/2).moveTo(-54,59).cylinder(5,41)).union(w0.sketch().push([(-42,-10)]).circle(28).reset().face(w0.sketch().segment((-49,56),(-27,25)).segment((-25,26)).segment((-46,58)).close().assemble()).finalize().extrude(95)).union(w1.workplane(offset=-75/2).moveTo(22.5,14).box(3,46,75))