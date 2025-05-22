import cadquery as cq
w0=cq.Workplane('YZ',origin=(45,0,0))
r=w0.sketch().segment((-100,-51),(-27,-51)).arc((95,26),(-46,-14)).segment((-100,-14)).close().assemble().finalize().extrude(-89)