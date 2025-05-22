import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,17,0))
w1=cq.Workplane('ZX',origin=(0,47,0))
r=w0.workplane(offset=25/2).moveTo(-60,11).cylinder(25,40).union(w1.sketch().segment((-34,-36),(-6,-36)).arc((33,-53),(71,-36)).segment((100,-36)).segment((100,36)).segment((71,36)).arc((33,53),(-6,36)).segment((-34,36)).close().assemble().finalize().extrude(-95))