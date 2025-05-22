import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-13,0))
r=w0.sketch().segment((-100,-32),(-79,-32)).segment((-94,-42)).segment((-87,-53)).segment((-58,-32)).segment((22,-32)).segment((22,-57)).segment((100,-57)).segment((100,57)).segment((22,57)).segment((22,26)).segment((-100,26)).close().assemble().finalize().extrude(26)