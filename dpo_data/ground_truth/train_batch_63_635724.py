import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-6))
w1=cq.Workplane('ZX',origin=(0,66,0))
r=w0.sketch().push([(0,55.5)]).rect(166,29).reset().face(w0.sketch().segment((-52,59),(-42,48)).segment((-31,57)).segment((-41,69)).close().assemble(),mode='s').finalize().extrude(-94).union(w1.workplane(offset=-136/2).moveTo(23,0).box(154,128,136))