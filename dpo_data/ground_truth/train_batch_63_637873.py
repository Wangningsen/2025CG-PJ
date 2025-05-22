import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('YZ',origin=(-6,0,0))
r=w0.sketch().segment((5,-44),(81,-75)).segment((100,-27)).segment((24,3)).close().assemble().finalize().extrude(-66).union(w0.sketch().arc((-58,29),(-62,-71),(-15,18)).segment((21,18)).segment((21,75)).segment((-58,75)).close().assemble().finalize().extrude(-37)).union(w1.sketch().push([(14.5,-69)]).rect(27,6).push([(22,-70)]).circle(2,mode='s').finalize().extrude(64))