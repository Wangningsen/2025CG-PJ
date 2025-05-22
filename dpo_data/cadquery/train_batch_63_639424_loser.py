import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-36))
r=w0.sketch().arc((-25,70),(4,-100),(19,72)).arc((-3,100),(-25,70)).assemble().push([(0,-13)]).circle(77,mode='s').finalize().extrude(72)