import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,87))
r=w0.workplane(offset=-174/2).moveTo(43,-49).box(4,30,174).union(w0.sketch().segment((-88,34),(16,34)).arc((27,32),(38,34)).segment((68,34)).segment((68,100)).segment((-88,100)).close().assemble().reset().face(w0.sketch().arc((-5,-52),(68,-92),(71,-12)).arc((4,34),(-5,-52)).assemble()).finalize().extrude(-153))