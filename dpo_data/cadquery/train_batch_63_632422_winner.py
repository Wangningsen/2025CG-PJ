import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,85))
r=w0.sketch().segment((-34,-100),(34,-67)).segment((6,-7)).arc((-2,48),(-34,100)).close().assemble().finalize().extrude(-170)