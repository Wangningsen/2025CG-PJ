import cadquery as cq
w0=cq.Workplane('YZ',origin=(59,0,0))
w1=cq.Workplane('ZX',origin=(0,18,0))
r=w0.sketch().segment((39,1),(41,1)).segment((41,-63)).arc((84,-30),(39,1)).assemble().finalize().extrude(-106).union(w0.workplane(offset=-87/2).moveTo(-31,-47).cylinder(87,53)).union(w1.workplane(offset=-21/2).moveTo(87,-41.5).box(26,35,21))