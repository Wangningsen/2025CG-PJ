import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-16))
r=w0.sketch().arc((-65,-11),(17,-25),(45,61)).arc((39,72),(29,78)).arc((-61,82),(-65,-11)).assemble().reset().face(w0.sketch().segment((-65,-1),(-23,-23)).segment((-1,21)).segment((-34,42)).close().assemble(),mode='s').finalize().extrude(-47).union(w0.workplane(offset=79/2).moveTo(39,-57).cylinder(79,43))