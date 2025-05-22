import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-56))
w1=cq.Workplane('ZX',origin=(0,-97,0))
r=w0.sketch().circle(100).rect(184,50,mode='s').finalize().extrude(153).union(w1.sketch().push([(-67,0)]).circle(34).circle(15,mode='s').finalize().extrude(95))