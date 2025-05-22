import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-7))
r=w0.sketch().arc((-43,1),(-27,-100),(-35,2)).arc((-51,100),(-43,1)).assemble().push([(-33,-49.5)]).rect(74,67,mode='s').finalize().extrude(-22).union(w0.sketch().arc((51,-47),(91,-36),(81,4)).arc((23,4),(51,-47)).assemble().finalize().extrude(37))