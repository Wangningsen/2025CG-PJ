import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-29,0))
w1=cq.Workplane('ZX',origin=(0,-58,0))
r=w0.workplane(offset=86/2).moveTo(11,8).cylinder(86,6).union(w1.sketch().arc((-89,-97),(-36,-9),(42,-76)).arc((54,86),(-77,-10)).arc((-99,-51),(-89,-97)).assemble().finalize().extrude(87))