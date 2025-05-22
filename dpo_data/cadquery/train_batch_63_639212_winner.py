import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,2,0))
w1=cq.Workplane('ZX',origin=(0,47,0))
r=w0.sketch().segment((-90,-37),(-5,-37)).segment((-5,-20)).segment((23,-20)).segment((23,100)).segment((-27,100)).segment((-27,-10)).segment((-90,-10)).close().assemble().finalize().extrude(-49).union(w1.sketch().segment((-36,-50),(23,-50)).segment((23,-100)).segment((31,-100)).segment((31,-50)).segment((90,-50)).segment((90,-32)).segment((31,-32)).segment((31,18)).segment((23,18)).segment((23,-32)).segment((-36,-32)).close().assemble().finalize().extrude(-23))