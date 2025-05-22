import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,52,0))
r=w0.sketch().push([(-35,51)]).circle(49).reset().face(w0.sketch().segment((-45,12),(-40,11)).segment((-24,96)).segment((-29,97)).close().assemble(),mode='s').finalize().extrude(-103).union(w0.sketch().push([(52,-65.5)]).rect(64,69).push([(25.5,-60)]).rect(5,2,mode='s').finalize().extrude(-72))