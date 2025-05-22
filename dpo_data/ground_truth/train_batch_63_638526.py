import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,18,0))
r=w0.sketch().arc((-32,-17),(-34,-99),(3,-27)).arc((20,97),(-32,-17)).assemble().finalize().extrude(-37)