import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-79))
r=w0.workplane(offset=104/2).moveTo(9.5,85.5).box(17,19,104).union(w0.workplane(offset=159/2).moveTo(0,-69).box(200,52,159))