import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-89,0))
r=w0.workplane(offset=71/2).moveTo(0,-18).box(174,164,71).union(w0.workplane(offset=178/2).moveTo(-35,58.5).box(52,83,178))