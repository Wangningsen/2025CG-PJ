import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().arc((-13,39),(-56,-65),(16,22)).arc((41,70),(7,29)).arc((0,33),(-8,35)).arc((-9,38),(-13,39)).assemble().finalize().extrude(-133).union(w0.workplane(offset=-100/2).moveTo(23,1).cylinder(100,60)).union(w0.workplane(offset=67/2).moveTo(18,0).cylinder(67,38))