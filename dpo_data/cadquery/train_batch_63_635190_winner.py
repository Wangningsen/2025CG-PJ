import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,54,0))
r=w0.sketch().push([(78,-27.5)]).rect(12,29).push([(83.5,-29)]).rect(1,6,mode='s').finalize().extrude(-108).union(w0.sketch().push([(-23,39)]).circle(61).push([(78,-40)]).rect(8,120).finalize().extrude(-43))