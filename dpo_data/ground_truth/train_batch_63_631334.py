import cadquery as cq
w0=cq.Workplane('YZ',origin=(-3,0,0))
r=w0.sketch().arc((-92,-35),(-59,-47),(-73,-79)).arc((-49,-98),(-18,-96)).arc((63,78),(-92,-35)).assemble().finalize().extrude(6)