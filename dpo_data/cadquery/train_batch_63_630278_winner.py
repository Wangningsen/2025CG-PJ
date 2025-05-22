import cadquery as cq
w0=cq.Workplane('YZ',origin=(-27,0,0))
r=w0.sketch().segment((-8,-47),(75,-47)).segment((75,88)).segment((-8,88)).segment((-8,50)).segment((26,50)).segment((26,29)).segment((-8,29)).close().assemble().push([(34,21)]).circle(14,mode='s').finalize().extrude(-73).union(w0.workplane(offset=127/2).moveTo(-22.5,-78.5).box(105,19,127))