import cadquery as cq
w0=cq.Workplane('YZ',origin=(-69,0,0))
r=w0.sketch().arc((-89,45),(58,-81),(-21,98)).arc((-18,30),(-89,45)).assemble().finalize().extrude(138)