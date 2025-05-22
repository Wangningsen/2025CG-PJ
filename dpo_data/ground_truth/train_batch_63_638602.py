import cadquery as cq
w0=cq.Workplane('YZ',origin=(-30,0,0))
r=w0.sketch().segment((-100,-1),(-76,-65)).segment((100,1)).segment((76,65)).close().assemble().finalize().extrude(61)