import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().circle(95).reset().face(w0.sketch().segment((-77,14),(-36,-5)).arc((-15,-35),(21,-32)).segment((61,-47)).segment((77,-14)).segment((36,5)).arc((15,35),(-21,32)).segment((-61,47)).close().assemble(),mode='s').finalize().extrude(-200)