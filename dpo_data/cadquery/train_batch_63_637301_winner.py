import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-56))
r=w0.sketch().segment((-81,-81),(81,-81)).segment((81,84)).segment((24,84)).segment((24,100)).segment((-63,100)).segment((-63,84)).segment((-81,84)).close().assemble().finalize().extrude(112).union(w0.workplane(offset=112/2).moveTo(0,-8).box(162,184,112))