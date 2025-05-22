import cadquery as cq
w0=cq.Workplane('YZ',origin=(-39,0,0))
r=w0.sketch().segment((-100,-43),(-75,-76)).segment((-29,-43)).arc((93,35),(-44,-14)).segment((-50,-6)).close().assemble().finalize().extrude(78)