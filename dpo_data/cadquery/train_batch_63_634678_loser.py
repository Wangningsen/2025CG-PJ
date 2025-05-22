import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-93))
r=w0.sketch().rect(200,86).push([(75,-28)]).circle(9,mode='s').finalize().extrude(186)