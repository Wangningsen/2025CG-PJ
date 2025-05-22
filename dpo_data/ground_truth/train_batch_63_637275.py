import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().arc((-75,47),(-22,-42),(76,-6)).arc((57,-10),(44,5)).segment((19,-27)).close().assemble().finalize().extrude(-200)