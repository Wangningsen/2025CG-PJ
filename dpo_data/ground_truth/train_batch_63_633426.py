import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,28,0))
r=w0.sketch().segment((-42,68),(-27,38)).arc((-17,38),(-8,36)).segment((20,50)).arc((23,52),(26,53)).segment((42,61)).segment((23,100)).segment((-22,78)).segment((-25,78)).segment((-25,76)).close().assemble().finalize().extrude(-57).union(w0.workplane(offset=-43/2).moveTo(-20,-80.5).box(30,39,43))