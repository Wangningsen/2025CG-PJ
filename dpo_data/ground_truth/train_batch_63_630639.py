import cadquery as cq
w0=cq.Workplane('YZ',origin=(47,0,0))
w1=cq.Workplane('YZ',origin=(52,0,0))
r=w0.sketch().segment((-46,-97),(-30,-97)).segment((-30,-100)).segment((-28,-96)).segment((-43,-89)).close().assemble().finalize().extrude(-99).union(w1.sketch().push([(3.5,88.5)]).rect(85,23).push([(12.5,83)]).rect(3,8,mode='s').finalize().extrude(-103))