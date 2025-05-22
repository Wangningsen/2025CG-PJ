import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,76))
r=w0.sketch().segment((-91,-44),(18,-100)).segment((91,44)).segment((-18,100)).close().assemble().finalize().extrude(-152)