import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().rect(104,130).push([(19,-28)]).rect(52,8,mode='s').reset().face(w0.sketch().segment((13,40),(21,39)).segment((22,49)).segment((14,50)).close().assemble(),mode='s').finalize().extrude(200)