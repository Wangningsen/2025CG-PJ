import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-14,0))
w1=cq.Workplane('ZX',origin=(0,-45,0))
r=w0.sketch().push([(-59,58)]).circle(36).reset().face(w0.sketch().segment((-80,61),(-78,44)).segment((-26,54)).segment((-29,72)).close().assemble(),mode='s').push([(-71.5,-94)]).rect(33,12).reset().face(w0.sketch().segment((-22,-10),(86,-20)).segment((95,76)).segment((-13,88)).close().assemble()).finalize().extrude(59).union(w1.sketch().push([(34,11)]).circle(18).circle(15,mode='s').finalize().extrude(7))