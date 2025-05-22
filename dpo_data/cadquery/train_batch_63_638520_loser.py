import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-67,14),(56,-40)).segment((67,-14)).segment((-56,40)).close().assemble().finalize().extrude(200)