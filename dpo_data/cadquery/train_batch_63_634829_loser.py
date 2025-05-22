import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
w1=cq.Workplane('ZX',origin=(0,70,0))
r=w0.sketch().segment((27,-11),(100,-11)).segment((100,75)).segment((36,75)).arc((-48,64),(27,16)).close().assemble().reset().face(w0.sketch().segment((27,22),(27,67)).arc((-41,44),(27,22)).assemble(),mode='s').finalize().extrude(-85).union(w0.workplane(offset=-80/2).moveTo(81,-84).cylinder(80,10)).union(w1.workplane(offset=-140/2).moveTo(-68,34.5).box(64,99,140))