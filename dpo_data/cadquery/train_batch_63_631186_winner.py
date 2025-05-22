import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,33,0))
r=w0.sketch().segment((-100,-71),(3,-71)).arc((52,-44),(100,-61)).segment((100,-35)).segment((27,-35)).segment((27,-3)).arc((-47,-3),(-81,71)).segment((-100,71)).close().assemble().finalize().extrude(-67)