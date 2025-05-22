import cadquery as cq
w0=cq.Workplane('YZ',origin=(-23,0,0))
r=w0.sketch().segment((-32,-2),(32,-2)).segment((32,2)).segment((10,2)).arc((8,1),(7,2)).segment((-32,2)).close().assemble().finalize().extrude(-77).union(w0.sketch().segment((-43,-15),(43,-15)).segment((43,1)).segment((-1,1)).segment((-1,15)).segment((-43,15)).close().assemble().finalize().extrude(123))