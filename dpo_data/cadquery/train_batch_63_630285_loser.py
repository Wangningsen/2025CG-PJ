import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-80))
r=w0.sketch().segment((-98,30),(-56,-35)).arc((-50,-69),(-26,-93)).segment((-22,-100)).segment((-14,-95)).arc((32,-93),(63,-57)).segment((98,-30)).segment((22,100)).close().assemble().finalize().extrude(23).union(w0.workplane(offset=160/2).cylinder(160,55))