import cadquery as cq
w0=cq.Workplane('YZ',origin=(17,0,0))
r=w0.sketch().push([(35,-34.5)]).rect(130,69).push([(-24.5,-20.5)]).rect(7,7,mode='s').finalize().extrude(-101).union(w0.sketch().arc((-100,41),(-49,48),(-98,33)).segment((-91,33)).arc((-56,48),(-93,41)).close().assemble().finalize().extrude(67))