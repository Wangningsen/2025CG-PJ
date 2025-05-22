import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-84))
r=w0.sketch().segment((-34,-100),(34,-67)).segment((6,-7)).arc((-3,51),(-34,100)).close().assemble().finalize().extrude(169)