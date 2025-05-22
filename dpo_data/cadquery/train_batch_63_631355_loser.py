import cadquery as cq
w0=cq.Workplane('YZ',origin=(-58,0,0))
w1=cq.Workplane('YZ',origin=(-38,0,0))
r=w0.sketch().arc((-31,-9),(-11,5),(12,-2)).arc((14,8),(11,18)).segment((34,87)).segment((13,94)).segment((1,52)).arc((-25,29),(-8,-1)).segment((-11,-9)).arc((-21,-7),(-31,-9)).assemble().reset().face(w0.sketch().segment((3,-97),(38,-100)).segment((48,24)).segment((13,27)).close().assemble()).finalize().extrude(20).union(w0.workplane(offset=117/2).moveTo(0,42.5).box(68,103,117)).union(w1.sketch().push([(0,43)]).circle(57).circle(41,mode='s').finalize().extrude(60))