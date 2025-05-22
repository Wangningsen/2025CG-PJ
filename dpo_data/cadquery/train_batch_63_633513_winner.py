import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-54,0))
r=w0.sketch().segment((33,79),(75,60)).segment((67,44)).segment((74,44)).segment((74,31)).segment((61,31)).segment((57,25)).segment((100,25)).segment((100,79)).close().assemble().finalize().extrude(54).union(w0.workplane(offset=109/2).moveTo(-70,-49).cylinder(109,30))