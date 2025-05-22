import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-50,0))
r=w0.sketch().segment((-100,-3),(-74,-3)).arc((-54,-63),(5,-35)).arc((96,30),(-15,13)).arc((-40,18),(-65,9)).segment((-65,44)).segment((-100,44)).close().assemble().finalize().extrude(100)