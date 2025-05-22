import cadquery as cq
w0=cq.Workplane('ZX',origin=(0,4,0))
r=w0.sketch().segment((43,-75),(87,-75)).arc((83,-55),(100,-41)).segment((90,-7)).segment((78,-10)).segment((85,-36)).segment((43,-36)).close().assemble().finalize().extrude(-58).union(w0.sketch().push([(-91.5,23)]).rect(17,104).push([(-92,23)]).circle(1,mode='s').finalize().extrude(50))