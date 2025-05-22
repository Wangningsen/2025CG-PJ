import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().circle(91).reset().face(w0.sketch().segment((-53,-12),(-16,-12)).arc((0,-20),(16,-12)).segment((53,-12)).segment((53,12)).segment((16,12)).arc((0,20),(-16,12)).segment((-53,12)).close().assemble(),mode='s').finalize().extrude(-200)