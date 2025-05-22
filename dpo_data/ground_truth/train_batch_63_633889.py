import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((-85,-99),(85,-99)).segment((85,-20)).arc((87,0),(85,20)).segment((85,99)).segment((-85,99)).segment((-85,20)).arc((-87,0),(-85,-20)).close().assemble().finalize().extrude(200)