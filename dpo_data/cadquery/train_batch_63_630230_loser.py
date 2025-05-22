import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-50,0))
r=w0.sketch().segment((-100,-3),(-74,-3)).arc((-53,-63),(5,-34)).arc((98,24),(-13,25)).arc((-41,18),(-65,6)).segment((-65,44)).segment((-100,44)).close().assemble().finalize().extrude(100)