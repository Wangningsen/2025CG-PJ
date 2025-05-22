import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,14))
r=w0.sketch().push([(56,77)]).circle(23).push([(61,97)]).circle(2,mode='s').finalize().extrude(-68).union(w0.sketch().segment((-79,-72),(-59,-100)).segment((-27,-76)).segment((-47,-49)).close().assemble().finalize().extrude(39))