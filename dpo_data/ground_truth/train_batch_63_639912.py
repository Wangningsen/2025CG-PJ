import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().circle(41).push([(-2,14)]).circle(18,mode='s').push([(25,20)]).circle(5,mode='s').push([(27.5,-1.5)]).rect(5,23,mode='s').finalize().extrude(-200)