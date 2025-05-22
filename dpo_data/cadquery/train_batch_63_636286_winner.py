import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,23))
r=w0.sketch().segment((-66,-100),(66,-100)).segment((66,3)).segment((25,3)).arc((-5,100),(-34,3)).segment((-66,3)).close().assemble().finalize().extrude(-58).union(w0.sketch().segment((-13,27),(3,27)).segment((3,62)).arc((-4,60),(-13,62)).close().assemble().finalize().extrude(12))