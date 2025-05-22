import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-21))
w1=cq.Workplane('YZ',origin=(-80,0,0))
r=w0.sketch().segment((-62,-76),(-60,-76)).segment((-60,-59)).arc((-22,-20),(-60,20)).segment((-60,37)).segment((-62,37)).segment((-62,20)).arc((-100,-20),(-62,-59)).close().assemble().finalize().extrude(96).union(w0.sketch().arc((21,66),(42,-59),(35,68)).arc((28,76),(21,66)).assemble().finalize().extrude(96)).union(w1.sketch().push([(-18,-42)]).circle(39).push([(-18.5,-42.5)]).rect(25,15,mode='s').finalize().extrude(10))