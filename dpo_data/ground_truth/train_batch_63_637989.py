import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().arc((-75,7),(29,-56),(56,62)).segment((26,9)).segment((20,12)).segment((20,7)).close().assemble().finalize().extrude(-200)