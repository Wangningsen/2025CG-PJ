import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-59,0))
w1=cq.Workplane('XY',origin=(0,0,90))
r=w0.workplane(offset=159/2).moveTo(76,-37).box(48,42,159).union(w1.sketch().push([(34,-76)]).circle(24).push([(30,-75)]).circle(18,mode='s').finalize().extrude(-190))