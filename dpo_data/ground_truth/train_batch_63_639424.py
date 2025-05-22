import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,35))
r=w0.sketch().arc((-26,70),(4,-100),(19,72)).arc((-5,100),(-26,70)).assemble().push([(0,-13)]).circle(77,mode='s').finalize().extrude(-71)