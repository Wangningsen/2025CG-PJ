import cadquery as cq
w0=cq.Workplane('YZ',origin=(30,0,0))
r=w0.sketch().rect(200,8).rect(8,6,mode='s').finalize().extrude(-59)