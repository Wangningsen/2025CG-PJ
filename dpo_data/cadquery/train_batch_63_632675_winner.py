import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-5,0))
w1=cq.Workplane('XY',origin=(0,0,11))
r=w0.sketch().arc((26,65),(-4,4),(61,-5)).segment((61,1)).segment((67,1)).arc((73,22),(68,43)).arc((79,53),(72,62)).arc((68,65),(64,67)).segment((64,68)).segment((58,68)).segment((58,8)).segment((26,8)).close().assemble().push([(32,-48)]).circle(20).finalize().extrude(-95).union(w1.sketch().segment((-53,30),(-2,30)).segment((-2,100)).segment((-53,100)).segment((-53,81)).arc((-51,79),(-53,77)).close().assemble().push([(-27.5,65)]).rect(49,68,mode='s').finalize().extrude(-91))