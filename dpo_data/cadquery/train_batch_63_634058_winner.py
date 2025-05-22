import cadquery as cq
w0=cq.Workplane('YZ',origin=(29,0,0))
r=w0.sketch().segment((-69,-84),(-36,-84)).segment((-36,-93)).segment((10,-93)).segment((10,-84)).segment((42,-84)).segment((42,-19)).arc((95,42),(13,23)).arc((-31,27),(-52,-10)).segment((-69,-10)).close().assemble().finalize().extrude(-115).union(w0.workplane(offset=57/2).moveTo(-87,80).cylinder(57,13))