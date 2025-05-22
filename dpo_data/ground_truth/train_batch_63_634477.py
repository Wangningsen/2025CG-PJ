import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,25,0))
w1=cq.Workplane('ZX',origin=(0,-12,0))
r=w0.sketch().push([(0,78.5)]).rect(66,43).reset().face(w0.sketch().segment((-13,67),(-3,62)).segment((-1,65)).arc((11,72),(10,86)).segment((13,90)).segment((3,95)).segment((1,92)).arc((-11,85),(-10,71)).close().assemble(),mode='s').finalize().extrude(-28).union(w1.sketch().push([(-15,-86)]).circle(14).push([(-22,-84)]).circle(6,mode='s').finalize().extrude(-13))