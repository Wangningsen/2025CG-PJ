import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-12))
r=w0.sketch().segment((30,-31),(59,-100)).segment((99,-83)).segment((55,15)).arc((-90,59),(30,-31)).assemble().finalize().extrude(25)