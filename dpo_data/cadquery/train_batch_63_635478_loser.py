import cadquery as cq
w0=cq.Workplane('YZ',origin=(-55,0,0))
r=w0.sketch().segment((-4,-4),(15,-30)).segment((32,-18)).arc((41,-18),(45,-10)).segment((51,-5)).arc((35,1),(29,18)).close().assemble().reset().face(w0.sketch().arc((43,34),(59,30),(64,13)).segment((100,32)).segment((80,60)).close().assemble()).finalize().extrude(42).union(w0.workplane(offset=109/2).moveTo(-56,-16).cylinder(109,44))