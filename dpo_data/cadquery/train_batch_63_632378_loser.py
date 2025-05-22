import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-98,42),(-37,-100)).segment((-27,-95)).arc((-18,-91),(-11,-85)).segment((-11,-88)).segment((-6,-87)).segment((-6,-99)).segment((6,-99)).segment((6,-86)).segment((11,-86)).segment((11,-97)).segment((38,-92)).segment((31,-74)).segment((98,-42)).segment((37,100)).close().assemble().finalize().extrude(-43)