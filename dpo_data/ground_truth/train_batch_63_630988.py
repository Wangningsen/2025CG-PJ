import cadquery as cq
w0=cq.Workplane('YZ',origin=(7,0,0))
r=w0.sketch().segment((-21,15),(-18,-19)).segment((21,-15)).segment((18,19)).close().assemble().finalize().extrude(-107).union(w0.workplane(offset=93/2).cylinder(93,28))