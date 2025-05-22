import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,86,0))
r=w0.workplane(offset=-186/2).moveTo(-99,-34).box(2,92,186).union(w0.sketch().push([(27,57)]).rect(146,46).reset().face(w0.sketch().segment((13,75),(27,35)).segment((41,40)).segment((27,80)).close().assemble(),mode='s').finalize().extrude(14))