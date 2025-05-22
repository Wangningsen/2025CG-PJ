import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,14,0))
r=w0.sketch().circle(100).push([(-82,-43)]).circle(2,mode='s').push([(80,14)]).rect(18,18,mode='s').finalize().extrude(-28)