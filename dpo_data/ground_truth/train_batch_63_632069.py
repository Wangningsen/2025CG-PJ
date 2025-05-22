import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-83,0))
r=w0.sketch().arc((-56,75),(-24,-97),(87,39)).arc((26,97),(-56,75)).assemble().finalize().extrude(166)