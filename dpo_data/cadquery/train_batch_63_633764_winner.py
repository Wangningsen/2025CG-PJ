import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().segment((-87,-42),(58,-77)).segment((87,42)).segment((-58,77)).close().assemble().finalize().extrude(-200)