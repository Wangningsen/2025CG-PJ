import cadquery as cq
w0=cq.Workplane('YZ',origin=(24,0,0))
r=w0.sketch().rect(64,24).push([(15,5)]).circle(2,mode='s').finalize().extrude(-124).union(w0.sketch().segment((-19,41),(-15,-43)).segment((19,-41)).segment((15,43)).close().assemble().rect(24,32,mode='s').finalize().extrude(76))