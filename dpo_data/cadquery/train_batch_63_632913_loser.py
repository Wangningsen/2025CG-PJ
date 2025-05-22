import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-16,0))
r=w0.sketch().push([(55,-37)]).circle(39).reset().face(w0.sketch().segment((36,-32),(55,-58)).segment((77,-42)).segment((58,-16)).close().assemble(),mode='s').finalize().extrude(-8).union(w0.workplane(offset=40/2).box(196,200,40))