import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,92))
r=w0.sketch().rect(200,86).push([(76,-26)]).circle(7,mode='s').finalize().extrude(-185)