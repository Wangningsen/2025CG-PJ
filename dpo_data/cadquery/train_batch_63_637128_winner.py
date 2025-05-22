import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,9))
r=w0.sketch().arc((-32,14),(-24,-99),(34,-3)).arc((70,53),(22,100)).segment((22,-12)).segment((7,-12)).segment((7,100)).arc((-37,66),(-32,14)).assemble().finalize().extrude(-19)