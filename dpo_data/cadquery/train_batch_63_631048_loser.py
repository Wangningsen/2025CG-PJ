import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,100))
r=w0.sketch().circle(21).push([(11.5,-5.5)]).rect(7,15,mode='s').finalize().extrude(-200)