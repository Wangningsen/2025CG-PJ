import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.sketch().arc((-99,-35),(-63,-40),(-44,-72)).segment((-37,-65)).segment((-4,-83)).segment((10,-72)).segment((100,-6)).segment((35,83)).segment((-60,14)).arc((-91,-2),(-99,-35)).assemble().push([(16,0)]).circle(36,mode='s').finalize().extrude(-96)