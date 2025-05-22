import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-44))
w1=cq.Workplane('XY',origin=(0,0,-44))
r=w0.sketch().push([(-33,41)]).circle(51).reset().face(w0.sketch().segment((-13,-100),(36,-100)).segment((-13,-70)).close().assemble()).finalize().extrude(49).union(w1.workplane(offset=88/2).moveTo(52,36).box(64,128,88))