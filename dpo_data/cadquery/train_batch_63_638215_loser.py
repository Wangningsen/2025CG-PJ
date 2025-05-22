import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,85))
r=w0.sketch().arc((-50,100),(-38,82),(-22,69)).segment((-22,70)).segment((-11,70)).segment((-11,63)).arc((-11,61),(-10,60)).segment((-11,60)).segment((-11,-100)).segment((11,-100)).segment((11,68)).arc((31,77),(50,100)).close().assemble().finalize().extrude(-170)