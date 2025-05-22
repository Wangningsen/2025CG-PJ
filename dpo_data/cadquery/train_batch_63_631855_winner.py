import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().circle(100).reset().face(w0.sketch().segment((-14,-73),(16,-73)).segment((16,-23)).arc((27,0),(16,22)).segment((16,70)).segment((-14,70)).segment((-14,22)).arc((-27,0),(-14,-23)).close().assemble(),mode='s').finalize().extrude(-57)