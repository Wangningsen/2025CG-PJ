import cadquery as cq
w0=cq.Workplane('YZ',origin=(-16,0,0))
w1=cq.Workplane('YZ',origin=(-17,0,0))
r=w0.sketch().push([(-24.5,-99.5)]).rect(115,1).push([(30,-76.5)]).rect(4,47).finalize().extrude(-53).union(w0.sketch().arc((23,90),(-67,37),(34,5)).arc((82,52),(23,89)).close().assemble().reset().face(w0.sketch().segment((-64,44),(-39,43)).segment((-39,62)).segment((-63,63)).close().assemble(),mode='s').push([(5,20.5)]).rect(40,61,mode='s').finalize().extrude(84)).union(w1.sketch().segment((29,4),(32,4)).segment((32,20)).arc((29,19),(29,20)).close().assemble().finalize().extrude(-2))