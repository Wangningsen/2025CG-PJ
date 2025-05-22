import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,23))
w1=cq.Workplane('ZX',origin=(0,2,0))
r=w0.sketch().push([(-41,35.5)]).rect(118,23).reset().face(w0.sketch().segment((-50,30),(-49,29)).segment((-45,35)).segment((-46,36)).close().assemble(),mode='s').push([(-16,30)]).circle(7,mode='s').finalize().extrude(8).union(w0.workplane(offset=67/2).moveTo(-41,35.5).box(18,23,67)).union(w1.sketch().segment((-90,-37),(-5,-37)).segment((-5,-20)).segment((23,-20)).segment((23,100)).segment((-27,100)).segment((-27,-10)).segment((-90,-10)).close().assemble().finalize().extrude(-49))