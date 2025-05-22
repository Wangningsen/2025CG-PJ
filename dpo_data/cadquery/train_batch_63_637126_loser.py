import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().circle(10).push([(-2,7.5)]).rect(4,3,mode='s').finalize().extrude(200)