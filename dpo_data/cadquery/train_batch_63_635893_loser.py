import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-100))
r=w0.sketch().rect(86,90).push([(27,0)]).circle(12,mode='s').finalize().extrude(200)