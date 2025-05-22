import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-4))
r=w0.sketch().push([(7,86)]).circle(14).push([(12,81)]).circle(4,mode='s').finalize().extrude(-21).union(w0.sketch().segment((-61,4),(-19,-100)).segment((61,-68)).segment((19,37)).close().assemble().finalize().extrude(28))