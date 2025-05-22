import cadquery as cq
w0=cq.Workplane('YZ',origin=(75,0,0))
r=w0.sketch().arc((-47,-94),(0,-82),(47,-94)).arc((1,94),(-47,-94)).assemble().finalize().extrude(-150)