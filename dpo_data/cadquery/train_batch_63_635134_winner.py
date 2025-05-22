import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-58,0))
r=w0.sketch().arc((-89,-97),(-21,-8),(42,-77)).arc((33,94),(-78,-21)).arc((-100,-56),(-89,-97)).assemble().finalize().extrude(88).union(w0.sketch().segment((1,15),(16,-1)).arc((13,10),(1,15)).assemble().finalize().extrude(117))