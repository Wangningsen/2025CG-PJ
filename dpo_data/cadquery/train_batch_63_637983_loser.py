import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,54))
r=w0.sketch().segment((52,82),(53,82)).segment((91,94)).segment((89,100)).close().assemble().finalize().extrude(-109).union(w0.sketch().segment((-91,-16),(-38,-16)).segment((-38,-100)).arc((-6,-43),(-10,23)).segment((-36,64)).segment((-77,7)).arc((-83,-4),(-91,-16)).assemble().push([(-30,-53)]).circle(5,mode='s').finalize().extrude(-63))