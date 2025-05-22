import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
r=w0.sketch().push([(8,86)]).circle(14).reset().face(w0.sketch().segment((3,81),(19,76)).segment((20,80)).segment((4,85)).close().assemble(),mode='s').finalize().extrude(-21).union(w0.sketch().segment((-61,4),(-19,-100)).segment((61,-68)).segment((19,36)).close().assemble().finalize().extrude(28))