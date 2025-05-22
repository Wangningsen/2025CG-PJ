import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-40,0))
r=w0.sketch().arc((-15,25),(-79,-79),(15,-1)).segment((45,-1)).arc((68,13),(91,-1)).segment((100,-1)).segment((100,94)).segment((-15,94)).close().assemble().finalize().extrude(80)