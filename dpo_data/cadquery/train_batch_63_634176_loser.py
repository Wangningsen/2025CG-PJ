import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-34))
r=w0.workplane(offset=-49/2).moveTo(-48,-23).cylinder(49,50).union(w0.sketch().push([(50.5,-14)]).rect(99,92).push([(72,-48)]).circle(4,mode='s').finalize().extrude(-22)).union(w0.sketch().segment((39,-21),(84,-21)).segment((84,-7)).segment((43,-7)).arc((-98,18),(39,-21)).assemble().finalize().extrude(116))