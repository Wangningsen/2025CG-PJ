import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,44,0))
w1=cq.Workplane('ZX',origin=(0,17,0))
r=w0.sketch().arc((40,61),(82,12),(66,76)).arc((49,76),(40,61)).assemble().finalize().extrude(-81).union(w0.sketch().segment((-100,12),(-60,-78)).segment((61,-34)).segment((32,37)).arc((-9,23),(-15,62)).segment((-22,59)).segment((-27,41)).close().assemble().finalize().extrude(2)).union(w1.sketch().arc((-8,-26),(31,-73),(2,-18)).segment((2,-4)).segment((-8,-4)).close().assemble().push([(21,-45)]).rect(12,34,mode='s').finalize().extrude(-63))