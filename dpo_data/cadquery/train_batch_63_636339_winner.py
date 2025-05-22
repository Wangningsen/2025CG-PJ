import cadquery as cq
w0=cq.Workplane('YZ',origin=(-23,0,0))
r=w0.workplane(offset=-77/2).box(64,4,77).union(w0.sketch().segment((-43,-15),(43,-15)).segment((43,1)).segment((-1,1)).segment((-1,15)).segment((-43,15)).close().assemble().finalize().extrude(123))