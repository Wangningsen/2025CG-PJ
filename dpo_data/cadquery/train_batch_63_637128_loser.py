import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,10))
r=w0.sketch().arc((-34,15),(-23,-99),(30,1)).arc((70,53),(22,99)).segment((22,-12)).segment((7,-12)).segment((7,100)).arc((-35,70),(-34,15)).assemble().finalize().extrude(-19)