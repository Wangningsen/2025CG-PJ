import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-83,0))
r=w0.sketch().segment((-33,-79),(66,-100)).segment((70,-80)).segment((-28,-60)).close().assemble().finalize().extrude(117).union(w0.workplane(offset=166/2).moveTo(-47,77).cylinder(166,23))