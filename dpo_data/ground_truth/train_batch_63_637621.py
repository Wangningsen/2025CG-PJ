import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,32,0))
w1=cq.Workplane('ZX',origin=(0,-32,0))
r=w0.sketch().arc((-2,37),(-92,-59),(38,-43)).arc((92,-18),(91,41)).segment((91,97)).arc((73,82),(71,59)).arc((30,63),(-2,37)).assemble().finalize().extrude(-43).union(w1.sketch().segment((-82,-96),(-63,-96)).segment((-63,-58)).arc((-75,-27),(-63,4)).segment((-63,41)).segment((-82,41)).close().assemble().finalize().extrude(54))