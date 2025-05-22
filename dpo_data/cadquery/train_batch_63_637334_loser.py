import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,32,0))
r=w0.sketch().arc((34,94),(-55,-84),(75,64)).arc((37,52),(34,94)).assemble().finalize().extrude(-65)