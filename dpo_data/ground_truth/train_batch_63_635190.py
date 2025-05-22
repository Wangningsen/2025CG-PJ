import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,54,0))
w1=cq.Workplane('ZX',origin=(0,52,0))
r=w0.sketch().push([(-23,39)]).circle(61).push([(78,-40)]).rect(8,120).finalize().extrude(-43).union(w1.sketch().push([(78,-27.5)]).rect(12,29).push([(82,-25)]).circle(2,mode='s').push([(82.5,-31)]).rect(1,2,mode='s').finalize().extrude(-106))