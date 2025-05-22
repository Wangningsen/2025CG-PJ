import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-34,0))
r=w0.sketch().segment((-100,-71),(3,-71)).arc((50,-44),(100,-61)).segment((100,-35)).segment((27,-35)).segment((27,-3)).arc((-51,0),(-81,71)).segment((-100,71)).close().assemble().finalize().extrude(68)