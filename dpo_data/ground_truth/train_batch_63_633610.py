import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-8,0))
r=w0.sketch().segment((-100,-10),(-80,-10)).arc((0,-81),(80,-10)).segment((100,-10)).segment((100,10)).segment((80,10)).arc((0,81),(-80,10)).segment((-100,10)).close().assemble().finalize().extrude(16)