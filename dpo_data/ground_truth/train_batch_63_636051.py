import cadquery as cq
w0=cq.Workplane('YZ',origin=(100,0,0))
r=w0.sketch().segment((-81,43),(67,-63)).segment((81,-43)).segment((-67,63)).close().assemble().finalize().extrude(-200)