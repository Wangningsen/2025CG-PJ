import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,5))
r=w0.sketch().segment((-100,-19),(-31,-59)).segment((7,7)).arc((100,11),(8,23)).segment((-54,59)).close().assemble().finalize().extrude(-11)