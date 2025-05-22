import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-21,0))
r=w0.sketch().segment((-98,42),(-37,-100)).segment((-7,-87)).segment((-5,-99)).segment((34,-93)).segment((31,-71)).segment((98,-42)).segment((37,100)).close().assemble().finalize().extrude(43)