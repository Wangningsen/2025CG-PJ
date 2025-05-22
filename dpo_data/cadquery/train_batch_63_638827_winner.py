import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((-11,-21),(11,3)).segment((-11,21)).close().assemble().finalize().extrude(200)