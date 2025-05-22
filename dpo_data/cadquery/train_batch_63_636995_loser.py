import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,48))
r=w0.sketch().push([(75,65)]).circle(20).push([(62,64)]).rect(10,12,mode='s').finalize().extrude(-148).union(w0.sketch().segment((-95,-59),(-63,-59)).arc((-15,-85),(33,-59)).segment((65,-59)).segment((65,3)).segment((33,3)).arc((-15,29),(-63,3)).segment((-95,3)).close().assemble().finalize().extrude(52))