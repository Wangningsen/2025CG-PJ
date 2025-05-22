import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
w1=cq.Workplane('ZX',origin=(0,24,0))
r=w0.sketch().arc((27,7),(30,1),(30,-5)).segment((30,-41)).arc((42,-31),(50,-19)).arc((91,16),(37,3)).arc((33,7),(27,7)).assemble().finalize().extrude(-67).union(w0.workplane(offset=-5/2).moveTo(-52,59).cylinder(5,41)).union(w0.sketch().push([(-42,-10)]).circle(28).reset().face(w0.sketch().segment((-49,55),(-35,32)).segment((-24,22)).segment((-46,58)).close().assemble()).finalize().extrude(95)).union(w1.workplane(offset=-3/2).moveTo(14,-63).box(46,74,3))