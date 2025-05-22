import cadquery as cq
w0=cq.Workplane('YZ',origin=(-67,0,0))
r=w0.sketch().arc((-5,-75),(95,-39),(42,56)).arc((-95,31),(-5,-75)).assemble().finalize().extrude(134)