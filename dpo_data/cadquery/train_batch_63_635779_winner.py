import cadquery as cq
w0=cq.Workplane('YZ',origin=(-58,0,0))
r=w0.sketch().segment((-100,-62),(92,-62)).segment((92,10)).segment((100,10)).segment((100,53)).segment((94,53)).segment((94,62)).segment((78,62)).segment((78,60)).segment((-100,60)).close().assemble().finalize().extrude(-10).union(w0.sketch().segment((50,-12),(63,1)).arc((55,-5),(50,-12)).assemble().finalize().extrude(127))