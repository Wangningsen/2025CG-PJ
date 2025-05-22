import cadquery as cq
w0=cq.Workplane('YZ',origin=(24,0,0))
w1=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-56,-95),(-53,-100)).segment((26,-42)).segment((22,-37)).close().assemble().finalize().extrude(-59).union(w1.sketch().arc((-14,7),(-54,-73),(34,-59)).segment((28,-59)).segment((28,-16)).arc((16,-3),(0,5)).segment((22,5)).arc((43,0),(64,5)).segment((100,5)).segment((100,88)).segment((64,88)).arc((43,94),(22,88)).segment((-14,88)).close().assemble().finalize().extrude(35))