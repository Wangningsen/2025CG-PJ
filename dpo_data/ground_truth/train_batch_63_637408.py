import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,40,0))
r=w0.workplane(offset=-97/2).moveTo(-48,-9).cylinder(97,52).union(w0.sketch().segment((13,39),(41,39)).arc((55,28),(71,36)).segment((72,51)).arc((56,61),(41,51)).segment((13,51)).close().assemble().reset().face(w0.sketch().segment((87,39),(100,39)).segment((100,51)).segment((88,51)).close().assemble()).finalize().extrude(16))