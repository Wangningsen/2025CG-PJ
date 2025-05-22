import cadquery as cq
w0=cq.Workplane('YZ',origin=(-69,0,0))
r=w0.sketch().arc((-90,44),(63,-78),(-21,98)).arc((-19,29),(-90,44)).assemble().finalize().extrude(138)