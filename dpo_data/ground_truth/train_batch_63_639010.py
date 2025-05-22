import cadquery as cq
w0=cq.Workplane('YZ',origin=(-80,0,0))
w1=cq.Workplane('XY',origin=(0,0,-21))
r=w0.sketch().push([(-19,-33)]).circle(42).circle(12,mode='s').finalize().extrude(10).union(w1.sketch().segment((-62,-76),(-60,-76)).segment((-60,-58)).arc((-33,-47),(-22,-20)).arc((91,-28),(30,68)).segment((30,76)).segment((21,76)).segment((21,66)).arc((-15,41),(-27,-1)).arc((-41,14),(-60,20)).segment((-60,37)).segment((-62,37)).segment((-62,20)).arc((-100,-19),(-62,-58)).close().assemble().finalize().extrude(97))