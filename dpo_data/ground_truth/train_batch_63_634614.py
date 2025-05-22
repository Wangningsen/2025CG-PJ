import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-48,-5),(-4,-5)).arc((18,21),(48,38)).segment((48,100)).segment((-48,100)).close().assemble().reset().face(w0.sketch().arc((-18,-46),(-26,-76),(-8,-100)).arc((-17,-74),(-18,-46)).assemble()).finalize().extrude(-42)