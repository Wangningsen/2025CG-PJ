import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-53,-75),(-25,-75)).arc((-14,-80),(-3,-81)).arc((35,-98),(50,-58)).segment((51,-58)).segment((51,30)).segment((-53,30)).close().assemble().finalize().extrude(-43).union(w0.sketch().segment((0,92),(25,24)).segment((53,34)).segment((24,100)).close().assemble().finalize().extrude(-15))