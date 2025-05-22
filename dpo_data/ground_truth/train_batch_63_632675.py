import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,-5,0))
w1=cq.Workplane('XY',origin=(0,0,11))
r=w0.sketch().segment((26,8),(26,65)).arc((7,-8),(73,28)).arc((79,53),(58,68)).segment((58,44)).segment((61,44)).segment((61,15)).segment((58,15)).segment((58,8)).close().assemble().push([(32,-48)]).circle(20).finalize().extrude(-95).union(w1.sketch().push([(-27.5,65)]).rect(51,70).push([(-27.5,65.5)]).rect(49,69,mode='s').finalize().extrude(-91))