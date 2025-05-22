import cadquery as cq
w0=cq.Workplane('YZ',origin=(13,0,0))
r=w0.sketch().arc((-74,-44),(-64,-19),(-74,6)).close().assemble().finalize().extrude(-113).union(w0.sketch().push([(65,36)]).circle(9).push([(66,34)]).rect(4,6,mode='s').finalize().extrude(87))