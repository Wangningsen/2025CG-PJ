import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,53))
r=w0.sketch().rect(200,84).reset().face(w0.sketch().segment((-99,-28),(-79,-29)).segment((-79,-26)).segment((-98,-25)).close().assemble(),mode='s').push([(44,29)]).circle(11,mode='s').finalize().extrude(-139).union(w0.workplane(offset=32/2).box(122,142,32))