import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().circle(41).push([(-2,14)]).circle(18,mode='s').push([(27.5,6)]).rect(5,38,mode='s').finalize().extrude(-200)