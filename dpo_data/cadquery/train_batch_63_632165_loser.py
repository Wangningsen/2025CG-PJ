import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-40,0))
r=w0.sketch().arc((-15,25),(-80,-77),(16,-1)).segment((47,-1)).arc((70,13),(93,-1)).segment((100,-1)).segment((100,94)).segment((-15,94)).close().assemble().finalize().extrude(80)