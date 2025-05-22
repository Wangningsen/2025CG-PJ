import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-31))
w1=cq.Workplane('XY',origin=(0,0,-66))
r=w0.sketch().segment((-100,-46),(-10,-46)).segment((-10,-23)).segment((-69,-23)).arc((-85,-36),(-100,-23)).close().assemble().finalize().extrude(4).union(w1.sketch().segment((4,-35),(21,-35)).segment((21,-46)).segment((79,-46)).segment((79,-35)).segment((100,-35)).segment((100,46)).segment((4,46)).close().assemble().push([(55,23)]).rect(4,22,mode='s').finalize().extrude(132))