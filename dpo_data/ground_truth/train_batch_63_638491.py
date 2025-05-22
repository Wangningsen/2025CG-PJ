import cadquery as cq
w0=cq.Workplane('YZ',origin=(28,0,0))
r=w0.sketch().segment((-9,20),(18,20)).arc((-29,89),(20,21)).segment((20,60)).segment((-9,60)).close().assemble().finalize().extrude(-81).union(w0.sketch().push([(13,-23)]).circle(30).push([(-6,-80)]).rect(14,40).finalize().extrude(26))