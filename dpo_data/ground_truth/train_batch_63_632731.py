import cadquery as cq
w0=cq.Workplane('XY',origin=(0,0,-43))
r=w0.sketch().segment((16,25),(24,3)).segment((100,30)).segment((79,90)).arc((71,76),(56,73)).arc((47,40),(16,25)).assemble().finalize().extrude(85).union(w0.workplane(offset=86/2).moveTo(-56,-46).cylinder(86,44))