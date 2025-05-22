import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
r=w0.sketch().segment((-58,-100),(25,-100)).segment((25,-73)).arc((52,-24),(25,19)).arc((13,100),(-17,23)).arc((-28,7),(-33,-11)).segment((-36,-11)).segment((-36,-1)).segment((-58,-1)).close().assemble().finalize().extrude(46)