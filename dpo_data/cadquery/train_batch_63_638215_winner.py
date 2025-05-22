import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,85))
r=w0.sketch().arc((-50,100),(-34,79),(-11,68)).segment((-11,-100)).segment((11,-100)).segment((11,68)).arc((34,79),(50,100)).close().assemble().finalize().extrude(-170)