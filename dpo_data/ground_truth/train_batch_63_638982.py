import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,64))
r=w0.sketch().rect(200,68).push([(0,-1.5)]).rect(36,19,mode='s').finalize().extrude(-128)