import cadquery as cq
w0=cq.Workplane('YZ',origin=(-100,0,0))
r=w0.sketch().segment((40,46),(40,53)).arc((-45,-49),(51,42)).segment((44,42)).segment((44,46)).close().assemble().push([(52,-40)]).circle(5,mode='s').finalize().extrude(200)