import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,34,0))
r=w0.sketch().rect(196,200).rect(26,172,mode='s').finalize().extrude(-68).union(w0.sketch().rect(200,130).circle(20,mode='s').finalize().extrude(-18))