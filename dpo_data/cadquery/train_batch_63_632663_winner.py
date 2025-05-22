import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-49,0))
r=w0.workplane(offset=-12/2).moveTo(-28.5,-45.5).box(109,109,12).union(w0.sketch().segment((60,56),(64,56)).segment((64,19)).segment((79,19)).segment((79,56)).segment((83,55)).segment((83,64)).segment((79,64)).segment((79,100)).segment((64,100)).segment((64,64)).segment((60,64)).close().assemble().finalize().extrude(111))