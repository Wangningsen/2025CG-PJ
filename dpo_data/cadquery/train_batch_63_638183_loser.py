import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().segment((-51,69),(-37,43)).arc((11,-68),(14,51)).segment((-13,59)).close().assemble().finalize().extrude(-200)