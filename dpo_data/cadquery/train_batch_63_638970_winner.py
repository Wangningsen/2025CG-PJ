import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-85,0))
w1=cq.Workplane('YZ',origin=(-1,0,0))
r=w0.workplane(offset=61/2).moveTo(32.5,0).box(43,188,61).union(w0.sketch().arc((-33,-62),(98,-27),(-3,63)).arc((-52,10),(-33,-62)).assemble().finalize().extrude(173)).union(w1.sketch().arc((9,-100),(41,-88),(69,-73)).arc((12,-16),(9,-100)).assemble().finalize().extrude(-75))