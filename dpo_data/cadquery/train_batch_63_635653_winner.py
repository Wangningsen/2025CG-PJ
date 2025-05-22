import cadquery as cq
w0=cq.Workplane('YZ',origin=(18,0,0))
w1=cq.Workplane('ZX',origin=(0,-7,0))
r=w0.workplane(offset=-118/2).moveTo(-10,23.5).box(66,121,118).union(w0.sketch().segment((-28,21),(62,-31)).segment((70,-17)).segment((-20,33)).close().assemble().finalize().extrude(-39)).union(w0.sketch().segment((-70,-19),(11,-19)).arc((39,-84),(51,-14)).segment((51,66)).segment((-70,66)).close().assemble().finalize().extrude(-28)).union(w1.sketch().segment((-79,41),(13,41)).segment((13,75)).segment((-8,75)).segment((-8,100)).segment((-79,100)).close().assemble().finalize().extrude(-24))