import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-4))
r=w0.sketch().arc((-6,84),(3,82),(2,74)).arc((19,95),(-6,84)).assemble().finalize().extrude(-21).union(w0.sketch().segment((-61,4),(-19,-100)).segment((61,-68)).segment((19,36)).close().assemble().finalize().extrude(28))