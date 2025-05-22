import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-100,0))
r=w0.sketch().circle(40).push([(-7.5,29)]).rect(9,16,mode='s').finalize().extrude(200)