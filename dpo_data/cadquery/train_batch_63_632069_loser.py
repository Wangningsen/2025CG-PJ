import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-83,0))
r=w0.sketch().arc((42,91),(-51,-86),(72,67)).arc((60,80),(42,91)).assemble().finalize().extrude(166)