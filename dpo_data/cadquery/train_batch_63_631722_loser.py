import cadquery as cq
w0=cq.Workplane('YZ',origin=(61,0,0))
w1=cq.Workplane('XY',origin=(0,0,-42))
r=w0.sketch().segment((-58,-11),(58,-11)).segment((58,100)).segment((-2,100)).arc((-15,55),(-58,37)).close().assemble().finalize().extrude(-125).union(w0.sketch().segment((-21,-22),(-10,-100)).segment((4,-98)).segment((-6,-21)).close().assemble().finalize().extrude(-36)).union(w1.sketch().segment((-23,-4),(18,-4)).arc((25,-21),(32,-4)).segment((64,-4)).segment((64,16)).segment((-23,16)).close().assemble().finalize().extrude(73))