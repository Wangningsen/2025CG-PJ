import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
w1=cq.Workplane('ZX',origin=(0,70,0))
r=w0.sketch().push([(-6,35)]).circle(58).rect(94,70,mode='s').finalize().extrude(-90).union(w0.sketch().push([(63.5,32)]).rect(73,86).push([(55,57)]).circle(5,mode='s').push([(82,-83)]).circle(10).finalize().extrude(-85)).union(w1.workplane(offset=-140/2).moveTo(-68,34.5).box(64,99,140))