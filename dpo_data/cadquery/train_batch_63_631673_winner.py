import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-26,0))
w1=cq.Workplane('XY',origin=(0,0,-16))
r=w0.sketch().push([(-65.5,-53.5)]).rect(37,93).push([(-65,-54)]).circle(4,mode='s').push([(1.5,54)]).rect(71,92).rect(49,68,mode='s').push([(44.5,-18)]).rect(79,70).finalize().extrude(115).union(w1.workplane(offset=85/2).moveTo(54,-57).box(20,64,85))