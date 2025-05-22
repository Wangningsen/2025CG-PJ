import cadquery as cq
w0=cq.Workplane('YZ',origin=(-68,0,0))
r=w0.sketch().segment((-100,-62),(92,-62)).segment((92,10)).segment((100,10)).segment((100,61)).segment((92,61)).segment((92,60)).segment((-100,60)).close().assemble().finalize().extrude(10).union(w0.sketch().segment((50,-12),(63,1)).segment((59,1)).close().assemble().finalize().extrude(136))