import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().segment((20,-74),(20,74)).arc((-20,0),(20,-74)).assemble().push([(4.5,24.5)]).rect(7,37,mode='s').finalize().extrude(200)