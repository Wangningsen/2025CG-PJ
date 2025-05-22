import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
w1=cq.Workplane('ZX',origin=(0,-4,0))
r=w0.sketch().segment((-58,-11),(58,-11)).segment((58,100)).segment((-2,100)).arc((-15,55),(-58,37)).close().assemble().finalize().extrude(-125).union(w0.sketch().segment((-21,-22),(-10,-100)).segment((4,-98)).segment((-8,-20)).close().assemble().finalize().extrude(-36)).union(w1.workplane(offset=20/2).moveTo(-5,20.5).box(74,87,20))