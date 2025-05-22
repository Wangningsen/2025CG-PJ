import cadquery as cq
w0=cq.Workplane('YZ',origin=(-14,0,0))
r=w0.sketch().arc((-89,73),(-16,-72),(99,43)).arc((0,29),(-89,73)).assemble().finalize().extrude(28)