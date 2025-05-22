import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
w1=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().arc((24,-14),(-46,-67),(42,-70)).segment((48,-70)).segment((48,100)).segment((24,100)).close().assemble().finalize().extrude(-42).union(w1.workplane(offset=42/2).moveTo(16.5,-35).box(11,6,42))