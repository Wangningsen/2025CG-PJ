import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,84))
r=w0.sketch().arc((-34,-100),(5,-81),(34,-66)).arc((6,0),(-18,80)).arc((-26,91),(-34,100)).close().assemble().finalize().extrude(-169)