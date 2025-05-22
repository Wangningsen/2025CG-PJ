import cadquery as cq
w0=cq.Workplane('YZ',origin=(0,0,0))
w1=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().segment((-13,31),(71,31)).segment((71,52)).segment((44,52)).segment((44,66)).segment((-13,66)).close().assemble().reset().face(w0.sketch().segment((28,45),(28,51)).arc((26,48),(28,45)).assemble(),mode='s').reset().face(w0.sketch().arc((30,45),(32,48),(30,51)).close().assemble(),mode='s').finalize().extrude(-100).union(w0.workplane(offset=100/2).moveTo(-22.5,27.5).box(97,55,100)).union(w1.workplane(offset=-83/2).moveTo(15.5,-22.5).box(95,61,83))