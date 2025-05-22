import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().circle(28).rect(52,10,mode='s').finalize().extrude(180).union(w0.sketch().segment((-16,0),(1,-16)).segment((16,0)).segment((-1,16)).close().assemble().finalize().extrude(200))