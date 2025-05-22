import cadquery as cq
w0=cq.Workplane('YZ',origin=(-6,0,0))
w1=cq.Workplane('ZX',origin=(0,51,0))
r=w0.sketch().push([(17,0)]).circle(83).push([(1,-77)]).circle(4,mode='s').finalize().extrude(30).union(w1.sketch().push([(0,-13)]).circle(12).push([(-5,-15)]).circle(4,mode='s').finalize().extrude(-151))