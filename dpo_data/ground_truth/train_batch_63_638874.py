import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
w1=cq.Workplane('XY',origin=(0,0,-9))
r=w0.sketch().segment((26,6),(30,6)).segment((30,-41)).segment((52,-22)).arc((90,18),(37,3)).segment((30,10)).close().assemble().finalize().extrude(-67).union(w0.workplane(offset=-5/2).moveTo(-53,59).cylinder(5,41)).union(w0.sketch().push([(-42,-10)]).circle(28).reset().face(w0.sketch().segment((-49,56),(-31,26)).arc((-28,25),(-25,23)).segment((-46,58)).close().assemble()).finalize().extrude(95)).union(w1.workplane(offset=46/2).moveTo(-63,22.5).box(74,3,46))