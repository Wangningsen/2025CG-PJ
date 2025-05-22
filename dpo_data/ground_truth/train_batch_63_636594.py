import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-3))
r=w0.workplane(offset=-29/2).moveTo(-7,-2.5).box(86,21,29).union(w0.sketch().push([(-79.5,15)]).rect(41,12).push([(-7,-2.5)]).rect(88,45).finalize().extrude(9)).union(w0.sketch().segment((49,-1),(100,-1)).segment((100,25)).segment((75,25)).arc((62,20),(49,19)).close().assemble().push([(74,12)]).circle(11,mode='s').finalize().extrude(36))