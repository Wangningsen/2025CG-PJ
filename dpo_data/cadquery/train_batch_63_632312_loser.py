import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().circle(100).push([(7,94)]).circle(5,mode='s').finalize().extrude(-43)