import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-13,-21),(13,21)).segment((-13,21)).close().assemble().finalize().extrude(-200)