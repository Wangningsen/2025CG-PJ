import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,43,0))
r=w0.sketch().segment((-49,90),(21,-100)).segment((49,-90)).segment((-21,100)).close().assemble().finalize().extrude(-87)