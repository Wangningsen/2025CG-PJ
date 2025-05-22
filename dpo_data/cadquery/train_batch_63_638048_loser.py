import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-32,0))
r=w0.sketch().push([(-67,16)]).circle(16).circle(3,mode='s').push([(34.5,0)]).rect(107,94).finalize().extrude(-68).union(w0.workplane(offset=132/2).moveTo(-67.5,16).box(41,26,132))