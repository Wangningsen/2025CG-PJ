import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-35))
r=w0.sketch().arc((-26,70),(3,-100),(19,72)).arc((-4,100),(-26,70)).assemble().push([(0,-13)]).circle(77,mode='s').finalize().extrude(71)