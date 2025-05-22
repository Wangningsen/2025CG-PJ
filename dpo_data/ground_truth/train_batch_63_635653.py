import cadquery as cq
w0=cq.Workplane('YZ',origin=(18,0,0))
w1=cq.Workplane('ZX',origin=(0,-7,0))
r=w0.workplane(offset=-118/2).moveTo(-10,23.5).box(66,121,118).union(w0.sketch().arc((-4,6),(37,-2),(59,-38)).arc((49,15),(-4,6)).assemble().finalize().extrude(-39)).union(w0.sketch().segment((-70,-19),(27,-19)).arc((37,-84),(47,-19)).segment((51,-19)).segment((51,66)).segment((-70,66)).close().assemble().finalize().extrude(-28)).union(w1.sketch().segment((-79,41),(13,41)).segment((13,75)).segment((-8,75)).segment((-8,100)).segment((-79,100)).close().assemble().finalize().extrude(-24))