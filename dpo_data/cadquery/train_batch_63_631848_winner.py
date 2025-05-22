import cadquery as cq
w0=cq.Workplane('YZ',origin=(18,0,0))
r=w0.sketch().segment((-43,87),(-25,87)).segment((-25,82)).segment((-5,82)).segment((-5,87)).segment((21,87)).segment((21,100)).segment((-43,100)).close().assemble().finalize().extrude(-36).union(w0.sketch().segment((-14,-96),(-5,-100)).segment((43,7)).segment((34,11)).close().assemble().finalize().extrude(-27))