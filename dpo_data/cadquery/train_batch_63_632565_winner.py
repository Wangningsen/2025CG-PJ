import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-14))
r=w0.sketch().segment((-64,91),(-49,61)).segment((-38,66)).arc((1,77),(-38,87)).segment((-44,100)).close().assemble().reset().face(w0.sketch().segment((52,-100),(61,-100)).segment((64,-35)).segment((55,-35)).close().assemble()).finalize().extrude(28)