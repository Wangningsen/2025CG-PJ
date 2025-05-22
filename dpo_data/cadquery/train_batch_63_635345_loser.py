import cadquery as cq
w0=cq.Workplane('YZ',origin=(-43,0,0))
w1=cq.Workplane('XY',origin=(0,0,10))
r=w0.sketch().push([(31,-44.5)]).rect(62,35).reset().face(w0.sketch().segment((37,-97),(38,-100)).segment((68,-95)).segment((67,-92)).close().assemble()).finalize().extrude(53).union(w1.sketch().segment((-31,-57),(-19,-57)).arc((6,-68),(31,-57)).segment((43,-57)).segment((43,-11)).segment((31,-11)).arc((6,-1),(-19,-11)).segment((-31,-11)).close().assemble().push([(7,-34)]).circle(7,mode='s').finalize().extrude(90))