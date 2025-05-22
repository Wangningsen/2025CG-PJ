import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-56))
r=w0.sketch().segment((-81,-100),(81,-100)).segment((81,84)).segment((24,84)).segment((24,100)).segment((-63,100)).segment((-63,84)).segment((-81,84)).close().assemble().finalize().extrude(112)