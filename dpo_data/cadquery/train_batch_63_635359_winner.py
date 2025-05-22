import cadquery as cq
w0=cq.Workplane('YZ',origin=(-39,0,0))
r=w0.sketch().segment((-100,-44),(-75,-77)).segment((-29,-43)).arc((95,30),(-44,-14)).segment((-52,-8)).close().assemble().finalize().extrude(78)