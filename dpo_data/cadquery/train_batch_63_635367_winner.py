import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().arc((-91,-19),(-26,-89),(66,-65)).close().assemble().reset().face(w0.sketch().segment((-66,65),(91,19)).arc((26,89),(-66,65)).assemble()).finalize().extrude(200)