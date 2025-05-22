import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,100,0))
w1=cq.Workplane('ZX',origin=(0,62,0))
r=w0.sketch().circle(61).circle(42,mode='s').finalize().extrude(-125).union(w1.workplane(offset=-162/2).cylinder(162,38))