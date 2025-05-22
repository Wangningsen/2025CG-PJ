import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-12,0))
w1=cq.Workplane('ZX',origin=(0,25,0))
r=w0.sketch().push([(-15,-86)]).circle(14).reset().face(w0.sketch().segment((-22,-86),(-21,-90)).segment((-17,-89)).segment((-18,-85)).close().assemble(),mode='s').finalize().extrude(-13).union(w1.sketch().push([(0,78.5)]).rect(66,43).push([(0,78)]).circle(13,mode='s').finalize().extrude(-28))