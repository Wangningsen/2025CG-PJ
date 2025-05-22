import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-56))
w1=cq.Workplane('ZX',origin=(0,-2,0))
r=w0.sketch().circle(100).rect(184,50,mode='s').finalize().extrude(153).union(w1.sketch().push([(-66,0)]).circle(31).push([(-72,0)]).circle(9,mode='s').finalize().extrude(-95))