import cadquery as cq
w0=cq.Workplane('YZ',origin=(-69,0,0))
r=w0.sketch().segment((-38,-100),(83,-100)).segment((83,-50)).segment((68,-50)).arc((-21,98),(-38,-73)).close().assemble().push([(65.5,-56.5)]).rect(25,7,mode='s').finalize().extrude(138)