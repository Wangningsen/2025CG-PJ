import cadquery as cq
w0=cq.Workplane('YZ',origin=(80,0,0))
r=w0.sketch().segment((-55,-75),(-5,-100)).segment((27,-36)).arc((36,-29),(39,-16)).segment((55,18)).segment((5,44)).close().assemble().push([(0,-28)]).circle(24,mode='s').finalize().extrude(-160).union(w0.workplane(offset=-78/2).moveTo(-26,92).cylinder(78,8))