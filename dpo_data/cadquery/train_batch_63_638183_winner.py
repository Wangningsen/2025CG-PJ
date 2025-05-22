import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-51,69),(-36,43)).arc((-1,-69),(39,40)).segment((37,42)).arc((2,54),(-32,64)).close().assemble().finalize().extrude(200)