import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-85))
r=w0.sketch().segment((-100,61),(-30,-93)).segment((19,-71)).arc((100,-49),(20,-18)).segment((-31,93)).close().assemble().finalize().extrude(170)