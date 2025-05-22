import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-52,0))
r=w0.workplane(offset=81/2).moveTo(-46,-24).cylinder(81,54).union(w0.sketch().segment((50,74),(58,74)).segment((54,78)).close().assemble().reset().face(w0.sketch().segment((95,34),(96,25)).segment((100,28)).close().assemble()).finalize().extrude(105))