import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,33,0))
w1=cq.Workplane('ZX',origin=(0,22,0))
r=w0.sketch().arc((8,30),(-64,-58),(16,23)).arc((48,66),(8,30)).assemble().finalize().extrude(-133).union(w0.workplane(offset=-100/2).moveTo(18,0).cylinder(100,65)).union(w1.workplane(offset=78/2).moveTo(18,0).cylinder(78,38))