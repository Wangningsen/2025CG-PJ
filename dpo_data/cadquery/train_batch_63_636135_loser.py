import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-51))
r=w0.sketch().segment((-100,-4),(28,-4)).arc((30,0),(32,-4)).segment((100,-4)).segment((100,4)).segment((-100,4)).close().assemble().finalize().extrude(107)