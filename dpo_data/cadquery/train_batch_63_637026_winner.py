import cadquery as cq
w0=cq.Workplane('YZ',origin=(21,0,0))
w1=cq.Workplane('YZ',origin=(20,0,0))
r=w0.sketch().arc((24,-13),(-44,-73),(45,-64)).segment((48,-64)).segment((48,100)).segment((24,100)).close().assemble().finalize().extrude(-42).union(w1.sketch().segment((18,-57),(37,-57)).arc((27,-51),(18,-44)).close().assemble().finalize().extrude(-21))