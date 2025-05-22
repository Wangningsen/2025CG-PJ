import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,21,0))
r=w0.sketch().segment((-53,-75),(-25,-75)).arc((-15,-77),(-4,-77)).arc((34,-98),(51,-58)).segment((51,30)).segment((-53,30)).close().assemble().finalize().extrude(-43).union(w0.sketch().segment((1,89),(23,25)).segment((47,34)).segment((25,100)).close().assemble().finalize().extrude(-15))