import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-22,0))
w1=cq.Workplane('ZX',origin=(0,22,0))
r=w0.sketch().arc((-36,32),(31,-33),(-26,40)).arc((-30,35),(-36,32)).assemble().finalize().extrude(16).union(w1.sketch().arc((4,100),(-13,-99),(25,97)).arc((13,92),(4,100)).assemble().finalize().extrude(-43))