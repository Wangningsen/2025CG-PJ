import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-22,0))
r=w0.sketch().segment((-98,42),(-37,-100)).segment((-14,-90)).segment((-12,-92)).segment((-11,-90)).segment((-10,-88)).segment((-5,-100)).segment((35,-92)).segment((31,-71)).segment((98,-42)).segment((37,100)).close().assemble().finalize().extrude(43)