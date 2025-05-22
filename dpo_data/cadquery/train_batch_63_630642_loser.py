import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-83))
r=w0.sketch().segment((-18,-100),(18,-100)).segment((18,20)).arc((22,32),(18,43)).segment((18,100)).segment((-18,100)).segment((-18,-20)).arc((-22,-35),(-18,-48)).close().assemble().finalize().extrude(166)