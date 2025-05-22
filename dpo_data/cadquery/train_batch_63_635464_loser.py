import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().rect(154,102).reset().face(w0.sketch().segment((-43,-28),(-26,-37)).segment((43,28)).segment((26,38)).close().assemble(),mode='s').finalize().extrude(200)