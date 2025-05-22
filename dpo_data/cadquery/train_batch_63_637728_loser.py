import cadquery as cq
w0=cq.Workplane('YZ',origin=(45,0,0))
r=w0.sketch().segment((-100,-51),(-28,-51)).arc((91,35),(-47,-14)).segment((-100,-14)).close().assemble().finalize().extrude(-89)