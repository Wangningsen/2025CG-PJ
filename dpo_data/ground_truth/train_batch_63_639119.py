import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-84,0))
r=w0.sketch().rect(200,14).rect(10,12,mode='s').finalize().extrude(169)