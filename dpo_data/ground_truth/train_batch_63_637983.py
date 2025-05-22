import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,54))
r=w0.sketch().segment((52,82),(91,94)).segment((89,100)).close().assemble().finalize().extrude(-109).union(w0.sketch().segment((-91,-16),(-38,-16)).segment((-38,-100)).arc((-3,-18),(-36,65)).close().assemble().push([(-27,-51)]).circle(3,mode='s').finalize().extrude(-63))