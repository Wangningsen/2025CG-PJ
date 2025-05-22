import cadquery as cq
w0=cq.Workplane('YZ',origin=(-69,0,0))
r=w0.sketch().arc((-73,-58),(0,-100),(73,-58)).segment((64,-58)).arc((78,-14),(64,30)).segment((73,30)).arc((0,71),(-73,30)).segment((-64,30)).arc((-78,-14),(-64,-58)).close().assemble().finalize().extrude(8).union(w0.sketch().push([(-43,83)]).rect(38,34).rect(10,12,mode='s').finalize().extrude(138))