import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-23,0))
r=w0.sketch().segment((-58,-100),(26,-100)).segment((26,-74)).arc((53,-34),(32,9)).arc((14,100),(-17,13)).arc((-27,7),(-35,-1)).segment((-58,-1)).close().assemble().finalize().extrude(46)