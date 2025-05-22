import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-4))
r=w0.sketch().segment((-88,-73),(-68,-73)).segment((-86,-88)).segment((-83,-92)).segment((-83,-100)).segment((-78,-100)).segment((-78,-94)).segment((-75,-97)).segment((-27,-61)).segment((-27,-73)).segment((95,-73)).segment((95,35)).segment((15,35)).arc((-50,99),(-88,19)).close().assemble().finalize().extrude(8)