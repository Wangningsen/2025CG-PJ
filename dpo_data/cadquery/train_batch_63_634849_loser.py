import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-50,0))
r=w0.sketch().segment((-26,-45),(66,-2)).segment((68,-6)).arc((88,64),(21,100)).arc((13,4),(-2,94)).arc((-17,90),(-26,78)).segment((13,78)).arc((1,62),(-3,42)).arc((-6,40),(-8,38)).arc((-98,-18),(-12,-98)).arc((-13,-97),(-13,-96)).arc((-18,-94),(-22,-92)).close().assemble().finalize().extrude(100)