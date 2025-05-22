import cadquery as cq
w0=cq.Workplane('YZ',origin=(-35,0,0))
w1=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-56,-95),(-53,-100)).segment((30,-41)).segment((27,-36)).close().assemble().finalize().extrude(59).union(w1.sketch().arc((-14,5),(-55,-72),(34,-60)).segment((28,-60)).segment((28,-19)).arc((18,-5),(3,4)).segment((22,4)).arc((43,0),(64,5)).segment((100,5)).segment((100,88)).segment((64,88)).arc((43,94),(22,88)).segment((-14,88)).close().assemble().finalize().extrude(35))