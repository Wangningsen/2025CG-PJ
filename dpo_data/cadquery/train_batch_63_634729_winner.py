import cadquery as cq
w0=cq.Workplane('YZ',origin=(75,0,0))
r=w0.sketch().arc((-46,-94),(1,-82),(48,-94)).arc((1,94),(-46,-94)).assemble().finalize().extrude(-150)