import cadquery as cq
w0=cq.Workplane('YZ',origin=(6,0,0))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.sketch().segment((-11,-96),(-9,-96)).arc((-6,-100),(-2,-96)).segment((0,-96)).segment((0,-95)).arc((5,-38),(-11,-93)).close().assemble().finalize().extrude(-15).union(w1.workplane(offset=90/2).moveTo(5,24).cylinder(90,4))