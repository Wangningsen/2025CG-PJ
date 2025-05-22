import cadquery as cq
w0=cq.Workplane('YZ',origin=(44,0,0))
w1=cq.Workplane('ZX',origin=(0,54,0))
r=w0.sketch().segment((19,-82),(34,-61)).segment((19,-61)).close().assemble().finalize().extrude(-131).union(w0.sketch().segment((-100,49),(-31,30)).segment((-21,63)).segment((-91,82)).close().assemble().finalize().extrude(43)).union(w1.sketch().arc((-70,-52),(-64,-47),(-58,-45)).segment((-58,-47)).segment((6,-47)).segment((6,-19)).arc((-31,-27),(-70,-19)).close().assemble().finalize().extrude(46))