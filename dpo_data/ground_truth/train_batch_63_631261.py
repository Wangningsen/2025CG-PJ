import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().rect(96,18).reset().face(w0.sketch().segment((-8,-6),(-3,-6)).segment((-3,-9)).segment((3,-9)).segment((3,-6)).segment((8,-6)).segment((8,6)).segment((3,6)).segment((3,9)).segment((-3,9)).segment((-3,6)).segment((-8,6)).close().assemble(),mode='s').finalize().extrude(200)