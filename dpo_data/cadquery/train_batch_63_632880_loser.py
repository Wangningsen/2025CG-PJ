import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().circle(40).push([(-7.5,27.5)]).rect(9,13,mode='s').finalize().extrude(200)