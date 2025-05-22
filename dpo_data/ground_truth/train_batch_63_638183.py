import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().arc((-51,69),(-44,52),(-37,42)).arc((8,-69),(32,45)).close().assemble().finalize().extrude(200)