import cadquery as cq
w0=cq.Workplane('YZ',origin=(35,0,0))
w1=cq.Workplane('YZ',origin=(36,0,0))
r=w0.sketch().segment((-64,33),(-43,33)).segment((-43,32)).segment((0,32)).segment((0,33)).segment((16,33)).segment((16,94)).segment((0,94)).segment((0,100)).segment((-43,100)).segment((-43,94)).segment((-64,94)).close().assemble().finalize().extrude(-94).union(w0.sketch().push([(20.5,-79.5)]).rect(87,41).push([(6,-90)]).circle(5,mode='s').finalize().extrude(-46)).union(w1.workplane(offset=22/2).moveTo(17,14).cylinder(22,4))