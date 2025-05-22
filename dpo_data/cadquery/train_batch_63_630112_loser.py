import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().circle(100).reset().face(w0.sketch().segment((-67,-6),(8,-6)).segment((8,70)).segment((-1,70)).segment((-1,95)).segment((-31,95)).segment((-31,70)).segment((-67,70)).close().assemble(),mode='s').finalize().extrude(-34)