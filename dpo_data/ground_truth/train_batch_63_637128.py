import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-10))
r=w0.sketch().arc((-33,15),(-29,-97),(38,-7)).arc((70,52),(22,100)).segment((22,-12)).segment((7,-12)).segment((7,100)).arc((-36,68),(-33,15)).assemble().finalize().extrude(19)