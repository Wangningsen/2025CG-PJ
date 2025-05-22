import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-55,0))
w1=cq.Workplane('YZ',origin=(-18,0,0))
r=w0.sketch().segment((-100,-9),(-52,-9)).segment((-52,-66)).arc((17,26),(-100,-9)).assemble().finalize().extrude(5).union(w1.sketch().push([(13,71.5)]).rect(84,57).push([(-4,89)]).circle(4,mode='s').finalize().extrude(87))