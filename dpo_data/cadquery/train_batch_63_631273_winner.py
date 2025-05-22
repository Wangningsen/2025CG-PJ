import cadquery as cq
w0=cq.Workplane('YZ',origin=(44,0,0))
w1=cq.Workplane('YZ',origin=(47,0,0))
r=w0.sketch().segment((-100,-57),(24,-57)).arc((69,-64),(26,-46)).segment((26,-11)).segment((-100,-11)).close().assemble().push([(89.5,58.5)]).rect(21,41).finalize().extrude(-91).union(w1.sketch().segment((45,-28),(47,-28)).segment((47,12)).arc((46,13),(47,14)).segment((47,46)).segment((45,46)).close().assemble().finalize().extrude(-94))