import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-27))
r=w0.sketch().arc((-7,21),(-99,-21),(2,-22)).arc((44,-43),(86,-22)).segment((100,-22)).segment((100,11)).segment((97,11)).arc((49,62),(-7,21)).assemble().reset().face(w0.sketch().arc((-8,6),(-90,-20),(-5,-9)).arc((-7,-2),(-8,6)).assemble(),mode='s').finalize().extrude(55)