import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,47,0))
r=w0.sketch().push([(-51,-28)]).circle(49).push([(-51.5,-28)]).rect(87,42,mode='s').finalize().extrude(-100).union(w0.sketch().arc((46,67),(51,-3),(51,68)).arc((48,69),(46,67)).assemble().finalize().extrude(-54)).union(w0.sketch().arc((12,32),(99,28),(16,52)).arc((21,40),(12,32)).assemble().finalize().extrude(6))