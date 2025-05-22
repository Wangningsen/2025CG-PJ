import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.sketch().arc((-99,-35),(-63,-40),(-45,-72)).arc((-34,-68),(-23,-58)).segment((-3,-83)).segment((100,-6)).segment((35,83)).segment((-59,13)).arc((-91,-2),(-99,-35)).assemble().push([(16,-1)]).circle(35,mode='s').finalize().extrude(-96)