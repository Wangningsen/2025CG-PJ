import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().circle(24).push([(0.5,0)]).rect(19,40,mode='s').finalize().extrude(-200)