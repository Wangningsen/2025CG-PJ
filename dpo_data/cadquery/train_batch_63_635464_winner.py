import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().rect(154,102).reset().face(w0.sketch().segment((-43,-28),(-31,-40)).segment((43,28)).segment((31,40)).close().assemble(),mode='s').finalize().extrude(-200)