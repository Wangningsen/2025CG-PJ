import cadquery as cq
w0=cq.Workplane('YZ',origin=(13,0,0))
r=w0.workplane(offset=-85/2).moveTo(-16,-81).cylinder(85,19).union(w0.sketch().segment((-9,39),(25,39)).segment((25,48)).arc((35,70),(25,92)).segment((25,100)).segment((-9,100)).segment((-9,92)).arc((-20,70),(-9,48)).close().assemble().finalize().extrude(58))