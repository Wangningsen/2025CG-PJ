import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,34))
r=w0.sketch().segment((-84,38),(-9,38)).segment((-9,46)).arc((66,61),(-9,76)).segment((-84,76)).close().assemble().push([(39,-55)]).circle(45).finalize().extrude(-77).union(w0.workplane(offset=9/2).moveTo(-31,-25).cylinder(9,32))