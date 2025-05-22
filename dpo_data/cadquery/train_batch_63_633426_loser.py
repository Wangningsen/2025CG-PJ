import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,29,0))
r=w0.sketch().segment((-42,68),(-27,38)).arc((-16,38),(-4,37)).segment((42,61)).segment((23,100)).segment((-24,77)).segment((-24,78)).segment((-25,78)).segment((-25,76)).close().assemble().finalize().extrude(-58).union(w0.workplane(offset=-44/2).moveTo(-20,-80.5).box(30,39,44))