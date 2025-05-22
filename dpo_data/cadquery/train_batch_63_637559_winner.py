import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-13,0))
r=w0.sketch().segment((-100,-32),(-76,-32)).segment((-94,-41)).segment((-90,-50)).segment((-55,-32)).segment((22,-32)).segment((22,-57)).segment((100,-57)).segment((100,57)).segment((22,57)).segment((22,26)).segment((-100,26)).close().assemble().finalize().extrude(26)