import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,92,0))
r=w0.sketch().circle(100).push([(-30,11)]).rect(34,100,mode='s').finalize().extrude(-184)