import cadquery as cq
w0=cq.Workplane('YZ',origin=(-12,0,0))
w1=cq.Workplane('ZX',origin=(0,41,0))
r=w0.workplane(offset=32/2).moveTo(-46.5,-42).box(49,116,32).union(w1.sketch().segment((-91,-46),(-42,-46)).segment((-42,-82)).segment((100,-82)).segment((100,-5)).segment((-5,-5)).segment((-5,49)).arc((-17,61),(-5,72)).segment((-5,82)).segment((-91,82)).close().assemble().push([(36.5,-24.5)]).rect(107,15,mode='s').finalize().extrude(30))