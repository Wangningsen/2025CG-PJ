import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.sketch().arc((-100,-35),(-64,-40),(-46,-72)).arc((-33,-67),(-23,-58)).segment((-4,-83)).segment((100,-6)).segment((35,83)).segment((-58,14)).arc((-90,-1),(-100,-35)).assemble().reset().face(w0.sketch().arc((-20,-4),(-16,-13),(-13,-22)).arc((48,14),(-20,-4)).assemble(),mode='s').finalize().extrude(-97)