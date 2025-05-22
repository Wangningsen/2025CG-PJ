import cadquery as cq
w0=cq.Workplane('YZ',origin=(44,0,0))
w1=cq.Workplane('ZX',origin=(0,54,0))
r=w0.sketch().arc((19,-82),(25,-71),(34,-61)).segment((19,-61)).close().assemble().finalize().extrude(-131).union(w0.sketch().segment((-100,49),(-31,30)).segment((-21,63)).segment((-91,82)).close().assemble().finalize().extrude(43)).union(w1.sketch().segment((-70,-47),(-68,-47)).segment((-68,-53)).segment((-62,-53)).segment((-62,-47)).segment((6,-47)).segment((6,-19)).arc((-29,-27),(-61,-22)).segment((-61,-20)).arc((-66,-19),(-70,-19)).close().assemble().finalize().extrude(46))