import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().segment((-58,-18),(-33,-52)).segment((-9,-34)).arc((-1,16),(48,10)).segment((58,18)).segment((33,52)).close().assemble().finalize().extrude(200)