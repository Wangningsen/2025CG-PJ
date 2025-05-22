import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,31,0))
w1=cq.Workplane('ZX',origin=(0,65,0))
r=w0.sketch().push([(12.5,-58.5)]).rect(97,83).push([(13,-58)]).circle(6,mode='s').reset().face(w0.sketch().segment((40,54),(41,50)).segment((97,71)).segment((95,75)).close().assemble()).finalize().extrude(-96).union(w1.workplane(offset=-30/2).moveTo(-62,65).cylinder(30,35))