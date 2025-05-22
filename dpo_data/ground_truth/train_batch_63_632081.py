import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,11,0))
w1=cq.Workplane('YZ',origin=(-85,0,0))
r=w0.sketch().push([(4,53)]).circle(47).push([(-4.5,44)]).rect(37,58,mode='s').finalize().extrude(12).union(w0.sketch().push([(-38,-87)]).circle(13).reset().face(w0.sketch().segment((-34,-90),(-32,-94)).segment((-30,-93)).segment((-32,-89)).close().assemble(),mode='s').finalize().extrude(84)).union(w1.sketch().push([(-69,-1.5)]).rect(52,53).push([(-53,5)]).circle(3,mode='s').finalize().extrude(170))