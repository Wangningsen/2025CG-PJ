import cadquery as cq
w0=cq.Workplane('YZ',origin=(32,0,0))
w1=cq.Workplane('YZ',origin=(8,0,0))
r=w0.workplane(offset=-16/2).moveTo(45,-19).cylinder(16,26).union(w0.sketch().segment((7,-36),(8,-36)).segment((8,-47)).segment((82,-47)).segment((82,-36)).segment((100,-36)).segment((100,-30)).segment((82,-30)).segment((82,9)).segment((8,9)).segment((8,-30)).segment((7,-30)).close().assemble().push([(53.5,-38.5)]).rect(3,5,mode='s').push([(53.5,-27)]).rect(3,6,mode='s').finalize().extrude(-6)).union(w1.workplane(offset=-40/2).moveTo(-55,2).cylinder(40,45))