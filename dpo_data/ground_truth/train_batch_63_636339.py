import cadquery as cq
w0=cq.Workplane('YZ',origin=(-23,0,0))
w1=cq.Workplane('YZ',origin=(-31,0,0))
r=w0.sketch().segment((-43,-15),(43,-15)).segment((43,1)).segment((-1,1)).segment((-1,15)).segment((-43,15)).close().assemble().finalize().extrude(123).union(w1.sketch().segment((-32,-2),(13,-2)).arc((14,1),(15,-2)).segment((32,-2)).segment((32,2)).segment((-22,2)).arc((-22,-1),(-24,1)).arc((-25,1),(-26,2)).segment((-32,2)).close().assemble().finalize().extrude(-69))