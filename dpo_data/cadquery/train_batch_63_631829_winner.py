import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().arc((-75,-60),(-43,-74),(-18,-95)).arc((48,83),(-75,-60)).assemble().finalize().extrude(200)