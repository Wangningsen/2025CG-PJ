import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-48,-5),(-8,-5)).segment((42,36)).segment((48,36)).segment((48,100)).segment((-48,100)).close().assemble().reset().face(w0.sketch().arc((-8,-100),(-17,-74),(-18,-46)).arc((-27,-71),(-8,-94)).close().assemble()).finalize().extrude(-42)