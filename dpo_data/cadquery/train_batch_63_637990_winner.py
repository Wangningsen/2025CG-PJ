import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-22,0))
w1=cq.Workplane('ZX',origin=(0,41,0))
r=w0.workplane(offset=-49/2).moveTo(-42,4).box(116,32,49).union(w1.sketch().segment((-91,-46),(-42,-46)).segment((-42,-82)).segment((100,-82)).segment((100,-5)).segment((-5,-5)).segment((-5,40)).arc((-15,60),(-5,79)).segment((-5,82)).segment((-91,82)).close().assemble().push([(36.5,-24.5)]).rect(107,15,mode='s').finalize().extrude(30))