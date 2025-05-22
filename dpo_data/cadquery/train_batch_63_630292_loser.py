import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,40))
w1=cq.Workplane('YZ',origin=(-50,0,0))
r=w0.sketch().arc((25,62),(-50,47),(26,33)).segment((100,33)).segment((100,62)).close().assemble().push([(-11,48)]).circle(20,mode='s').finalize().extrude(-92).union(w1.sketch().segment((-87,43),(-60,43)).arc((-61,47),(-60,52)).segment((-87,52)).close().assemble().finalize().extrude(-50))