import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,86,0))
r=w0.workplane(offset=-186/2).moveTo(-99,-34).box(2,92,186).union(w0.sketch().push([(27,57)]).rect(146,46).circle(10,mode='s').push([(32,39)]).circle(2,mode='s').finalize().extrude(14))