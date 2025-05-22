import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,17))
r=w0.sketch().rect(200,174).rect(132,138,mode='s').finalize().extrude(-34)