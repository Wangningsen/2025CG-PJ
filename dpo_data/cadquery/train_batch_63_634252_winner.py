import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-73,0))
r=w0.sketch().segment((-85,-100),(85,-100)).segment((85,-19)).arc((87,0),(85,19)).segment((85,100)).segment((-85,100)).segment((-85,19)).arc((-87,0),(-85,-19)).close().assemble().circle(86,mode='s').finalize().extrude(145)