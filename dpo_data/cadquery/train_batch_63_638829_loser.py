import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-53,0))
r=w0.workplane(offset=82/2).moveTo(-46,-24).cylinder(82,54).union(w0.sketch().segment((50,74),(55,72)).segment((58,76)).segment((53,78)).arc((52,75),(50,74)).assemble().reset().face(w0.sketch().segment((95,34),(96,25)).segment((100,28)).close().assemble()).finalize().extrude(106))