import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
w1=cq.Workplane('XY',origin=(0,0,72))
r=w0.sketch().push([(-23,39)]).circle(61).push([(78,-40)]).rect(8,120).finalize().extrude(43).union(w1.sketch().push([(-27.5,-4.5)]).rect(29,99).push([(-27,-4)]).circle(5,mode='s').finalize().extrude(12))