import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().circle(41).push([(3,14)]).circle(17,mode='s').push([(27.5,1)]).rect(5,28,mode='s').finalize().extrude(200)