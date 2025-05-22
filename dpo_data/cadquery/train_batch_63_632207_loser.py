import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-54))
r=w0.workplane(offset=30/2).moveTo(-70,-30).cylinder(30,30).union(w0.sketch().segment((-3,30),(31,30)).arc((50,19),(68,30)).segment((100,30)).segment((100,49)).segment((68,49)).arc((50,60),(31,49)).segment((-3,49)).close().assemble().push([(41.5,38.5)]).rect(5,29,mode='s').finalize().extrude(108))