import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().rect(174,76).reset().face(w0.sketch().segment((-26,20),(-22,-15)).segment((-15,-15)).arc((2,-23),(17,-16)).segment((26,-16)).segment((22,20)).segment((15,19)).arc((-2,23),(-17,15)).close().assemble(),mode='s').finalize().extrude(-200)