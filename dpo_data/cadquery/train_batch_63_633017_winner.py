import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,35,0))
w1=cq.Workplane('ZX',origin=(0,36,0))
r=w0.sketch().segment((49,-47),(51,-47)).segment((51,-46)).arc((49,-46),(49,-47)).assemble().finalize().extrude(-57).union(w1.workplane(offset=-71/2).cylinder(71,100))