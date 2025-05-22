import cadquery as cq
w0=cq.Workplane('YZ',origin=(-28,0,0))
w1=cq.Workplane('YZ',origin=(-27,0,0))
r=w0.sketch().segment((1,20),(8,19)).segment((9,27)).segment((2,28)).close().assemble().finalize().extrude(-35).union(w1.sketch().arc((-7,46),(-11,-99),(18,44)).segment((18,100)).segment((-7,100)).close().assemble().finalize().extrude(91))