import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,41,0))
w1=cq.Workplane('YZ',origin=(20,0,0))
r=w0.sketch().segment((-91,-46),(-42,-46)).segment((-42,-82)).segment((100,-82)).segment((100,-5)).segment((-5,-5)).segment((-5,82)).segment((-91,82)).close().assemble().push([(-14,-24.5)]).rect(6,15,mode='s').push([(44,-24.5)]).rect(92,15,mode='s').push([(-14,59)]).circle(3,mode='s').finalize().extrude(30).union(w1.workplane(offset=-32/2).moveTo(-46.5,-42).box(49,116,32))