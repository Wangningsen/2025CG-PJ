import cadquery as cq
w0=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().arc((-74,-44),(-64,-19),(-74,6)).close().assemble().finalize().extrude(-113).union(w0.sketch().segment((69,38),(69,43)).segment((70,43)).arc((60,29),(72,41)).segment((72,38)).close().assemble().push([(65.5,35)]).rect(3,8,mode='s').finalize().extrude(87))