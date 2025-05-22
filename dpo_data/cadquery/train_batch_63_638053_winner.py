import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.workplane(offset=-200/2).moveTo(0,19).box(136,26,200).union(w0.sketch().arc((27,-27),(32,-28),(37,-32)).arc((41,-12),(27,-27)).assemble().finalize().extrude(-55))