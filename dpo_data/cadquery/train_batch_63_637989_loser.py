import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().arc((-74,7),(34,-54),(56,62)).arc((39,31),(16,7)).close().assemble().finalize().extrude(-200)