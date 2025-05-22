import cadquery as cq
w0=cq.Workplane('YZ',origin=(-82,0,0))
r=w0.sketch().segment((-100,-14),(59,-14)).segment((59,-73)).segment((100,-40)).segment((11,73)).close().assemble().finalize().extrude(164)