import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
w1=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().segment((-4,85),(16,49)).arc((10,66),(-4,85)).assemble().finalize().extrude(-15).union(w0.sketch().arc((51,-100),(54,-81),(51,-62)).close().assemble().finalize().extrude(27)).union(w1.workplane(offset=15/2).moveTo(-51,35).box(6,130,15))