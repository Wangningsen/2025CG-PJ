import cadquery as cq
w0=cq.Workplane('YZ',origin=(8,0,0))
w1=cq.Workplane('XY',origin=(0,0,41))
r=w0.workplane(offset=-108/2).moveTo(-48,-45.5).box(98,65,108).union(w0.sketch().segment((35,-7),(35,34)).segment((36,34)).segment((36,59)).segment((58,59)).segment((58,34)).segment((97,34)).arc((16,76),(35,-7)).assemble().finalize().extrude(92)).union(w1.sketch().push([(41,47)]).rect(28,10).push([(41.5,47)]).rect(3,8,mode='s').finalize().extrude(-128))