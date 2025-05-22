import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
r=w0.sketch().circle(100).push([(-17,20)]).circle(49,mode='s').finalize().extrude(-200)