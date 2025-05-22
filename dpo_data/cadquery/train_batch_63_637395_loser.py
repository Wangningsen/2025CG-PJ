import cadquery as cq
w0=cq.Workplane('YZ',origin=(-40,0,0))
w1=cq.Workplane('YZ',origin=(-44,0,0))
r=w0.sketch().segment((-41,-36),(-39,-36)).arc((-24,-19),(-8,-36)).segment((-6,-36)).segment((-6,9)).segment((-41,9)).close().assemble().reset().face(w0.sketch().segment((64,-100),(81,-94)).segment((75,-82)).segment((64,-87)).close().assemble()).finalize().extrude(84).union(w1.workplane(offset=57/2).moveTo(-52,71).cylinder(57,29))