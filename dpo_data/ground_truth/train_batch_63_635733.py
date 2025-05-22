import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,4))
r=w0.sketch().segment((-89,-88),(-83,-100)).segment((-47,-82)).segment((-51,-73)).segment((95,-73)).segment((95,35)).segment((15,35)).arc((-50,99),(-88,16)).segment((-88,-73)).segment((-59,-73)).close().assemble().finalize().extrude(-8)