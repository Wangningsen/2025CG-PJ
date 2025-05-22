import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-41))
r=w0.sketch().rect(200,108).push([(4,-12)]).circle(18,mode='s').finalize().extrude(82)