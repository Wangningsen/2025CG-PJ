import cadquery as cq
w0=cq.Workplane('YZ',origin=(-57,0,0))
r=w0.sketch().segment((-100,-16),(-52,-16)).segment((-52,-94)).segment((100,-94)).segment((100,94)).segment((-52,94)).segment((-52,72)).segment((-100,72)).close().assemble().finalize().extrude(115)