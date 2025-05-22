import cadquery as cq
w0=cq.Workplane('YZ',origin=(-21,0,0))
r=w0.sketch().arc((24,-13),(-44,-72),(45,-61)).segment((48,-61)).segment((48,100)).segment((24,100)).close().assemble().finalize().extrude(41)