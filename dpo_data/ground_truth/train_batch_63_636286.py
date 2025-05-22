import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,22))
r=w0.sketch().segment((-66,-100),(66,-100)).segment((66,3)).segment((24,3)).arc((-5,100),(-34,3)).segment((-66,3)).close().assemble().finalize().extrude(-58).union(w0.workplane(offset=13/2).moveTo(-5,47).box(16,38,13))