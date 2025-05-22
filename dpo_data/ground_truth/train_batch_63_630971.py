import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().segment((-83,38),(-9,38)).segment((-9,46)).arc((66,61),(-9,76)).segment((-83,76)).close().assemble().reset().face(w0.sketch().segment((7,-87),(8,-87)).arc((72,-25),(7,-86)).close().assemble()).finalize().extrude(-77).union(w0.workplane(offset=9/2).moveTo(-30,-24).cylinder(9,33))