import cadquery as cq
w0=cq.Workplane('YZ',origin=(39,0,0))
w1=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().arc((-15,90),(11,94),(38,90)).segment((38,100)).segment((-15,100)).close().assemble().finalize().extrude(-112).union(w1.workplane(offset=-93/2).moveTo(65,-30).cylinder(93,8))