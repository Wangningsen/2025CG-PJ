import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-19,0))
r=w0.sketch().arc((-31,-17),(-37,-98),(5,-27)).arc((23,97),(-31,-17)).assemble().finalize().extrude(38)