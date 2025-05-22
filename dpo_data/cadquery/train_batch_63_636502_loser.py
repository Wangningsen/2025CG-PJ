import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,52,0))
r=w0.sketch().push([(-35,51)]).circle(49).reset().face(w0.sketch().segment((-46,13),(-41,12)).segment((-25,97)).segment((-30,98)).close().assemble(),mode='s').finalize().extrude(-103).union(w0.sketch().push([(52,-65.5)]).rect(64,69).push([(27,-62)]).circle(3,mode='s').finalize().extrude(-72))