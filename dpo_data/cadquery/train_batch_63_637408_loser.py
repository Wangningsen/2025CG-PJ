import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,40,0))
r=w0.workplane(offset=-96/2).moveTo(-48,-9).cylinder(96,52).union(w0.sketch().segment((13,39),(41,39)).arc((56,28),(72,39)).segment((100,39)).segment((100,51)).segment((72,51)).arc((56,61),(41,51)).segment((13,51)).close().assemble().finalize().extrude(17))